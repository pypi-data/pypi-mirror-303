
#### SpliceAI Modules
from keras.models import load_model
from pkg_resources import resource_filename
from spliceai.utils import one_hot_encode
import numpy as np
import tensorflow as tf

# Check if GPU is available
if tf.config.list_physical_devices('GPU'):
    print("Running on GPU.")
else:
    print("Running on CPU.")

# tf.config.threading.set_intra_op_parallelism_threads(1)
# tf.config.threading.set_inter_op_parallelism_threads(1)

sai_paths = ('models/spliceai{}.h5'.format(x) for x in range(1, 6))
sai_models = [load_model(resource_filename('spliceai', x)) for x in sai_paths]



def sai_predict_probs(seq: str, models: list) -> list:
    '''
    Predicts the donor and acceptor junction probability of each
    NT in seq using SpliceAI.

    Let m:=2*sai_mrg_context + L be the input seq length. It is assumed
    that the input seq has the following structure:

          seq = |<sai_mrg_context NTs><L NTs><sai_mrg_context NTs>|

    The returned probability matrix is of size 2XL, where
    the first row is the acceptor probability and the second row
    is the donor probability. These probabilities corresponds to the
    middel <L NTs> NTs of the input seq.
    '''
    x = one_hot_encode(seq)[None, :]
    y = np.mean([models[m].predict(x, verbose=0) for m in range(5)], axis=0)
    # return y[0, :, 1:].T
    y = y[0, :, 1:].T
    return y[0, :], y[1, :]


def run_spliceai_seq(seq, indices, threshold=0):
    # seq = 'N' * 5000 + seq + 'N' * 5000
    ref_seq_probs_temp = sai_predict_probs(seq, sai_models)
    ref_seq_acceptor_probs, ref_seq_donor_probs = ref_seq_probs_temp[0, :], ref_seq_probs_temp[1, :]
    acceptor_indices = {a: b for a, b in list(zip(indices, ref_seq_acceptor_probs)) if b >= threshold}
    donor_indices = {a: b for a, b in list(zip(indices, ref_seq_donor_probs)) if b >= threshold}
    return acceptor_indices, donor_indices