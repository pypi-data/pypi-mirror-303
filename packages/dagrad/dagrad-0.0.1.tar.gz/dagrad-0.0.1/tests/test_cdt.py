import os
os.environ['R_HOME'] = '/Library/Frameworks/R.framework/Resources'  # Correct path to R
os.environ['R_USER'] = "/Users/duntrain/Library/R/arm64/4.4/library" 
from dagrad.daglearner import learning_dag
# from cdt.metrics import SHD_CPDAG
from dagrad.utils import utils, profiler
import numpy as np

def generate_linear_uneq_data(n,d,s0,graph_type,sem_type,seed=1234):
        std_low, std_high = 0.1, 0.5
        utils.set_random_seed(seed=seed)
        B_true = utils.simulate_dag(d, s0, graph_type)
        W_true = utils.simulate_parameter(B_true)
        std = np.random.uniform(std_low, std_high, d)
        Omega =np.diag(std**2)
        X = utils.simulate_linear_sem(W_true, n, sem_type, std)
        return X, W_true, Omega

from causallearn.graph.Dag import Dag
from causallearn.graph.GraphNode import GraphNode
from causallearn.utils.DAG2PAG import dag2pag
from causallearn.utils.DAG2CPDAG import dag2cpdag
from causallearn.graph.SHD import SHD

def create_graph_from_W(W):
    d = W.shape[0]
    nodes = []
    for k in range(d):
        nodes.append(GraphNode(f"X{int(k)+1}"))
    dag = Dag(nodes)
    nonzero_indices = np.where(W != 0)
    for i, j in zip(*nonzero_indices):
        dag.add_directed_edge(nodes[i], nodes[j])
    return dag

def shd_cpdag(W0,W1):
    if isinstance(W0, np.ndarray):
        W0 = create_graph_from_W(W0)
        W0 = dag2cpdag(W0)
    if isinstance(W1, np.ndarray):
        W1 = create_graph_from_W(W1)
        W1 = dag2cpdag(W1)
    
    return SHD(W0,W1).get_shd()
if __name__ == '__main__':
    seed = np.random.randint(1, 1000)
    print(f'We are working with seed : {seed}')
    n, d, s0, graph_type, sem =1000, 10, 20, 'ER', 'gauss'
    X, W_true, Omega = generate_linear_uneq_data(n,d,s0,graph_type,sem,seed = seed)
    W_est = learning_dag(X,method = 'dagma', general_options={'w_threshold':0.0})
    method = 'dagma'
    model = 'linear'
    reg = 'mcp'
    loss_fn = 'logll'
    optimizer = 'adam'

    # print(SHD_CPDAG(W_true!=0, utils.threshold_W(W_est.copy(),threshold=0.3)!=0))
    print(shd_cpdag(W_true, utils.threshold_W(W_est)))

    general_options = {'lambda1': 0.1, 'gamma': 0.2, 'initialization': W_est}
    method_options = {'mu_init':0.0001, 'T':4, 'verbose': False}
    # method_options = {'rho': 1000.0,  'verbose': False}

    # learning_dag = profiler.profile_function(learning_dag)
    import cProfile
    cProfile.run('W_est = learning_dag(X, method=method, model=model, reg=reg, loss_fn=loss_fn, optimizer=optimizer, general_options=general_options, method_options=method_options)', 'output.prof')
    # snakeviz output.prof
    W_est =  learning_dag(X, method = method, 
                model = model, 
                reg = reg, 
                loss_fn = loss_fn, 
                optimizer = optimizer,
                general_options = general_options,
                method_options = method_options,)

    print(shd_cpdag(W_true, W_est))
    # from pyinstrument import Profiler
    # profiler = Profiler()
    # profiler.start()

    # W_est =  learning_dag(X, method = method, 
    #              model = model, 
    #              reg = reg, 
    #              loss_fn = loss_fn, 
    #              optimizer = optimizer,
    #              general_options = general_options,
    #              method_options = method_options,)

    # profiler.stop()
    # print(profiler.output_text(unicode=True, color=True))

    # print(W_est)
    # print(SHD_CPDAG(W_true!=0, W_est!=0))
    # print(shd_cpdag(W_true, W_est))

