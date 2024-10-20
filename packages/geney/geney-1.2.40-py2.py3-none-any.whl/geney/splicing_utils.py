import networkx as nx
import numpy as np
from .mutation_utils import get_mutation
from .seqmat_utils import Gene


class SpliceSite:
    def __init__(self, pos, ss_type, prob):
        self.pos = pos
        self.ss_type = ss_type  # 0 for donors, 1 for acceptors
        self.prob = prob

class SpliceSiteFactory:
    @staticmethod
    def create_splice_site(pos, ss_type, prob):
        return SpliceSite(pos, ss_type, prob)

def compute_paths_sequential(G, transcript, exon_starts, exon_ends):
    """
    Compute paths from start to end and from end to start sequentially, then return the paths with their probabilities.
    """
    new_paths = {}
    prob_sum = 0

    # Combine paths in both directions
    all_paths = list(nx.all_simple_paths(G, transcript.transcript_start, transcript.transcript_end)) + \
                list(nx.all_simple_paths(G, transcript.transcript_end, transcript.transcript_start))

    # Compute the probabilities of each path sequentially
    path_probs = [path_weight_mult(G, path, 'weight') for path in all_paths]

    # Populate new_paths dictionary with computed paths and probabilities
    for i, (path, curr_prob) in enumerate(zip(all_paths, path_probs)):
        prob_sum += curr_prob
        new_paths[i] = {
            'acceptors': sorted([p for p in path if p in exon_starts and p != transcript.transcript_start], reverse=transcript.rev),
            'donors': sorted([p for p in path if p in exon_ends and p != transcript.transcript_end], reverse=transcript.rev),
            'path_weight': curr_prob
        }
    return new_paths, prob_sum


def develop_aberrant_splicing(transcript, aberrant_splicing):
    # Prepare exon start and end dictionaries
    exon_starts = prepare_splice_sites(transcript.acceptors, transcript.transcript_start, aberrant_splicing, 'acceptors')
    exon_ends = prepare_splice_sites(transcript.donors, transcript.transcript_end, aberrant_splicing, 'donors')

    # Create SpliceSite nodes and filter based on probability > 0
    nodes = [
        SpliceSiteFactory.create_splice_site(pos, 0, prob) for pos, prob in exon_ends.items()
    ] + [
        SpliceSiteFactory.create_splice_site(pos, 1, prob) for pos, prob in exon_starts.items()
    ]
    nodes = [s for s in nodes if s.prob > 0]

    # Sort nodes based on position, respecting transcript direction
    nodes.sort(key=lambda x: x.pos, reverse=transcript.rev)

    # Create the directed graph
    G = create_splice_graph(nodes, transcript.rev)

    # Compute new paths and their probabilities sequentially
    new_paths, prob_sum = compute_paths_sequential(G, transcript, exon_starts, exon_ends)

    # Normalize probabilities and filter based on threshold
    new_paths = normalize_and_filter_paths(new_paths, prob_sum)

    return list(new_paths.values())


def prepare_splice_sites(transcript_sites, transcript_boundary, aberrant_splicing, site_type):
    """
    Prepare and return a dictionary of splice sites (acceptors or donors) including transcript boundaries
    and aberrant splicing information.
    """
    site_dict = {v: 1 for v in transcript_sites}
    site_dict.update({transcript_boundary: 1})
    site_dict.update({s: v['absolute'] for s, v in aberrant_splicing[f'missed_{site_type}'].items()})
    site_dict.update({s: v['absolute'] for s, v in aberrant_splicing[f'discovered_{site_type}'].items()})
    return site_dict


def create_splice_graph(nodes, reverse_direction):
    """
    Create and return a directed graph with splice sites as nodes and edges based on splice site type
    and probability of occurrence.
    """
    G = nx.DiGraph()
    G.add_nodes_from([n.pos for n in nodes])

    for i in range(len(nodes)):
        trailing_prob = 0
        in_between = set()
        curr_node = nodes[i]

        for j in range(i + 1, len(nodes)):
            next_node = nodes[j]
            in_between.add(next_node.ss_type)

            if curr_node.ss_type != next_node.ss_type:
                new_prob = next_node.prob - trailing_prob
                if new_prob > 0:
                    G.add_edge(curr_node.pos, next_node.pos, weight=new_prob)
                    trailing_prob += next_node.prob
    return G


def normalize_and_filter_paths(new_paths, prob_sum):
    """
    Normalize path probabilities and filter out paths with a probability less than 0.01.
    """
    for i, d in new_paths.items():
        d['path_weight'] = round(d['path_weight'] / prob_sum, 3)
    new_paths = {k: v for k, v in new_paths.items() if v['path_weight'] > 0.00001}
    return new_paths


def path_weight_mult(G, path, weight):
    """
    Calculate the multiplicative weight of the path.
    """
    cost = 1
    for node, nbr in zip(path[:-1], path[1:]):
        cost *= G[node][nbr][weight]
    return cost


# Missplicing Detection
def find_ss_changes(ref_dct, mut_dct, known_splice_sites, threshold=0.5):
    '''
    :param ref_dct:  the spliceai probabilities for each nucleotide (by genomic position) as a dictionary for the reference sequence
    :param mut_dct:  the spliceai probabilities for each nucleotide (by genomic position) as a dictionary for the mutated sequence
    :param known_splice_sites: the indices (by genomic position) that serve as known splice sites
    :param threshold: the threshold for detection (difference between reference and mutated probabilities)
    :return: two dictionaries; discovered_pos is a dictionary containing all the positions that meat the threshold for discovery
            and deleted_pos containing all the positions that meet the threshold for missing and the condition for missing
    '''

    new_dict = {v: mut_dct.get(v, 0) - ref_dct.get(v, 0) for v in
                list(set(list(ref_dct.keys()) + list(mut_dct.keys())))}

    discovered_pos = {k: {'delta': round(float(v), 3), 'absolute': round(float(mut_dct[k]), 3), 'reference': round(ref_dct[k], 3)} for k, v in
                      new_dict.items() if v >= threshold} # and k not in known_splice_sites}   # if (k not in known_splice_sites and v >= threshold) or (v > 0.45)}

    deleted_pos = {k: {'delta': round(float(v), 3), 'absolute': round(float(mut_dct.get(k, 0)), 3), 'reference': round(ref_dct[k], 3)} for k, v in
                   new_dict.items() if -v >= threshold} # and k in known_splice_sites}      #if k in known_splice_sites and v <= -threshold}

    return discovered_pos, deleted_pos


def find_transcript_missplicing(transcript, mutations, context=5000, window=2500, threshold=0.5, engine='spliceai'):
    from functools import reduce

    ref = transcript.pre_mrna
    # for mutation in mutations:
    #     var = ref + mutation

    var = reduce(lambda acc, mutation: acc + mutation, mutations, ref)

    center = int(np.mean([mutation.position for mutation in mutations]) // 1)

    total_context = context + window

    length = ref.seqmat.shape[-1]
    center_index = ref.rel_pos(center)
    ref_start_pad = max(0, total_context - center_index)
    ref_end_pad = max(0, total_context - (length - center_index))

    length = var.seqmat.shape[-1]
    center_index = var.rel_pos(center)
    var_start_pad = max(0, total_context - center_index)
    var_end_pad = max(0, total_context - (length - center_index))

    ref = ref.inspect(center, context=total_context)
    var = var.inspect(center, context=total_context)
    #
    # ref_indices = np.concatenate([np.zeros(ref_start_pad), ref.inspect(center, context = window).indices, np.zeros(ref_end_pad)])
    # mut_indices = np.concatenate([np.zeros(var_start_pad), var.inspect(center, context = window).indices, np.zeros(var_end_pad)])

    ref_indices = np.concatenate([np.zeros(ref_start_pad), ref.indices, np.zeros(ref_end_pad)])
    mut_indices = np.concatenate([np.zeros(var_start_pad),  var.indices, np.zeros(var_end_pad)])

    ref_indices = ref_indices[context:-context]
    mut_indices = mut_indices[context:-context]

    ref_seq = 'N'*ref_start_pad + ref.seq + 'N'*ref_end_pad
    var_seq = 'N'*var_start_pad + var.seq + 'N'*var_end_pad

    # print(f"PAdding: {ref_start_pad}, {ref_end_pad}")
    if engine == 'spliceai':
        from .spliceai_utils import sai_predict_probs, sai_models
        ref_seq_acceptor_probs, ref_seq_donor_probs = sai_predict_probs(ref_seq, models=sai_models)
        mut_seq_acceptor_probs, mut_seq_donor_probs = sai_predict_probs(var_seq, models=sai_models)
        # ref_seq_acceptor_probs, ref_seq_donor_probs = ref_seq_probs_temp[0, :], ref_seq_probs_temp[1, :]
        # mut_seq_acceptor_probs, mut_seq_donor_probs = mut_seq_probs_temp[0, :], mut_seq_probs_temp[1, :]

    elif engine == 'pangolin':
        from .pangolin_utils import pangolin_predict_probs, pang_models
        ref_seq_donor_probs, ref_seq_acceptor_probs = pangolin_predict_probs(ref_seq, models=pang_models)
        mut_seq_donor_probs, mut_seq_acceptor_probs = pangolin_predict_probs(var_seq, models=pang_models)

    else:
        raise ValueError(f"{engine} not implemented")

    visible_donors = np.intersect1d(transcript.donors, ref_indices)
    visible_acceptors = np.intersect1d(transcript.acceptors, ref_indices)

    assert len(ref_indices) == len(ref_seq_acceptor_probs), f'Reference pos ({len(ref_indices)}) not the same as probs ({len(ref_seq_acceptor_probs)})'
    assert len(mut_indices) == len(mut_seq_acceptor_probs), f'Mut pos ({len(mut_indices)}) not the same as probs ({len(mut_seq_acceptor_probs)})'

    iap, dap = find_ss_changes({p: v for p, v in list(zip(ref_indices, ref_seq_acceptor_probs))},
                               {p: v for p, v in list(zip(mut_indices, mut_seq_acceptor_probs))},
                               visible_acceptors,
                               threshold=threshold)

    assert len(ref_indices) == len(ref_seq_donor_probs), 'Reference pos not the same'
    assert len(mut_indices) == len(mut_seq_donor_probs), 'Mut pos not the same'

    idp, ddp = find_ss_changes({p: v for p, v in list(zip(ref_indices, ref_seq_donor_probs))},
                               {p: v for p, v in list(zip(mut_indices, mut_seq_donor_probs))},
                               visible_donors,
                               threshold=threshold)

    ref_acceptors = {a: b for a, b in list(zip(ref_indices, ref_seq_acceptor_probs))}
    ref_donors = {a: b for a, b in list(zip(ref_indices, ref_seq_donor_probs))}

    lost_acceptors = {int(p): {'absolute': np.float64(0), 'delta': round(float(-ref_acceptors[p]), 3)} for p in
                      visible_acceptors if p not in mut_indices and p not in dap}
    lost_donors = {int(p): {'absolute': np.float64(0), 'delta': round(float(-ref_donors[p]), 3)} for p in visible_donors
                   if p not in mut_indices and p not in ddp}
    dap.update(lost_acceptors)
    ddp.update(lost_donors)

    missplicing = {'missed_acceptors': dap, 'missed_donors': ddp, 'discovered_acceptors': iap, 'discovered_donors': idp}
    missplicing = {outk: {float(k): v for k, v in outv.items()} for outk, outv in missplicing.items()}
    temp =  {outk: {int(k) if k.is_integer() else k: v for k, v in outv.items()} for outk, outv in missplicing.items()}
    return temp


class Missplicing:
    def __init__(self, splicing_dict, threshold=0.5):
        self.missplicing = splicing_dict
        self.threshold = threshold

    # def __repr__(self):
    #     return f'Missplicing({self.modification.mut_id}) --> {self.missplicing}'

    def __str__(self):
        return self.aberrant_splicing

    def __bool__(self):
        if self.apply_sai_threshold_alt() is not None:
            return True
        return False

    def __iter__(self):
        vals = [0]
        for event, details in self.missplicing.items():
            for e, d in details.items():
                vals.append(d['delta'])
        return iter(vals)

    # def __eq__(self, alt_splicing):
    #     flag, _ = self.check_splicing_difference(self.missplicing, alt_splicing, self.threshold)
    #     return not flag

    @property
    def aberrant_splicing(self):
        return self.apply_sai_threshold(self.threshold)

    def apply_sai_threshold(self, threshold=None):
        splicing_dict = self.missplicing
        if not threshold:
            threshold = self.threshold

        new_dict = {}
        for event, details in self.missplicing.items():
            in_dict = {}
            for e, d in details.items():
                if abs(d['delta']) >= threshold:
                    in_dict[e] = d
                    # return splicing_dict
            new_dict[event] = in_dict
        return new_dict

    def apply_sai_threshold_alt(self, splicing_dict=None, threshold=None):
        splicing_dict = self.missplicing if not splicing_dict else splicing_dict
        threshold = self.threshold if not threshold else threshold
        for event, details in splicing_dict.items():
            for e, d in details.items():
                if abs(d['delta']) >= threshold:
                    return splicing_dict
        return None

    def get_max_missplicing_delta(self):
        max_delta = 0
        for event, details in self.missplicing.items():
            for e, d in details.items():
                if abs(d['delta']) > max_delta:
                    max_delta = abs(d['delta'])
        return max_delta


def find_transcript_splicing(transcript, engine='spliceai'):
    ref = transcript.pre_mrna
    ref_start_pad = 5000
    ref_end_pad = 5000

    ref_indices = ref.indices
    ref_seq = 'N' * ref_start_pad + ref.seq + 'N' * ref_end_pad
    if engine == 'spliceai':
        from .spliceai_utils import sai_predict_probs, sai_models
        ref_seq_acceptor_probs, ref_seq_donor_probs = sai_predict_probs(ref_seq, sai_models)

    elif engine == 'pangolin':
        from .pangolin_utils import pangolin_predict_probs, pang_models
        ref_seq_donor_probs, ref_seq_acceptor_probs = pangolin_predict_probs(ref_seq, models=pang_models)

    else:
        raise ValueError(f"{engine} not implemented")

    assert len(ref_seq_donor_probs) == len(ref_indices), f'{len(ref_seq_donor_probs)}  vs. {len(ref_indices)}'
    donor_probs = {i: p for i, p in list(zip(ref_indices, ref_seq_donor_probs))}
    donor_probs = dict(sorted(donor_probs.items(), key=lambda item: item[1], reverse=True))

    acceptor_probs = {i: p for i, p in list(zip(ref_indices, ref_seq_acceptor_probs))}
    acceptor_probs = dict(sorted(acceptor_probs.items(), key=lambda item: item[1], reverse=True))
    return donor_probs, acceptor_probs


def benchmark_splicing(gene, organism='hg38', engine='spliceai'):
    gene = Gene(gene, organism=organism)
    transcript = gene.transcript()
    if len(transcript.introns) == 0:
        return None, None

    transcript.generate_pre_mrna()
    predicted_donor_sites, predicted_acceptor_sites = find_transcript_splicing(transcript, engine=engine)
    num_introns = len(transcript.introns)
    predicted_donors = list(predicted_donor_sites.keys())[:num_introns]
    predicted_acceptors = list(predicted_acceptor_sites.keys())[:num_introns]
    correct_donor_preds = [v for v in predicted_donors if v in transcript.donors]
    correct_acceptor_preds = [v for v in predicted_acceptors if v in transcript.acceptors]
    return len(correct_donor_preds) / num_introns, len(correct_acceptor_preds) / num_introns, len(transcript.introns)


def missplicing(mut_id, splicing_threshold=0.5, primary_transcript=True, organism='hg38', engine='spliceai'):
    gene = Gene(mut_id.split(':')[0], organism=organism)
    mutation = get_mutation(mut_id, rev=gene.rev)
    results = {}

    for tid, transcript in gene.run_transcripts():
        # if not transcript.primary_transcript and primary_transcript:
        #     continue
        #
        if mutation not in transcript:
            continue

        good_tid = tid

        transcript.generate_pre_mrna()
        results[tid] = Missplicing(find_transcript_missplicing(transcript, mutation, engine=engine),
                                   threshold=splicing_threshold)

    # if len(results) == 0:
    #     return None
    #
    # if primary_transcript and good_tid in results:
    #     return results[good_tid]
    # else:
    #     return None

    return results

