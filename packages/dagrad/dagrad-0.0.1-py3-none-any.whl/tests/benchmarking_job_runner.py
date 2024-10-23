import os
from dagrad.daglearner import learning_dag
import numpy as np
import time
from dagrad.utils import utils
from notears.notears.linear import notears_linear
from notears.notears.nonlinear import notears_nonlinear, NotearsMLP
from dagma.linear import DagmaLinear
from dagma.nonlinear import DagmaNonlinear,DagmaMLP
from dagrad.utils.topo_utils import set_sizes_linear, set_sizes_nonlinear
from topo.topo_linear import TOPO_linear, regress, score
from topo.topo_utils import threshold_W
from topo.topo_nonlinear import TopoMLP, TOPO_Nonlinear
import pandas as pd

def generate_nonlinear_data(n,d,s0,graph_type,sem_type,seed=1234):
        utils.set_random_seed(seed=seed)
        B_true = utils.simulate_dag(d, s0, graph_type)
        X = utils.simulate_nonlinear_sem(B_true, n, sem_type)
        return X, B_true

def generate_linear_data(n,d,s0,graph_type,sem_type,seed=1234):
        utils.set_random_seed(seed=seed)
        B_true = utils.simulate_dag(d, s0, graph_type)
        W_true = utils.simulate_parameter(B_true)
        X = utils.simulate_linear_sem(W_true, n, sem_type)
        return X, W_true, B_true

def save_results(result_dict, path):
    columns = list(result_dict.keys())
    sem = result_dict['sem']
    d = result_dict['d']
    k = result_dict['k']
    graph = result_dict['graph']
    method = result_dict['method']   
    PD = pd.DataFrame(columns=columns)
    name = f"{d}_{graph}_{k}_{method}_{sem}"
    PD.loc[len(PD.index)] = list(result_dict.values())
    if os.path.isfile(path + name + '.csv'):
        PD.to_csv(path + name + '.csv', mode='a', index=False, header=False)
    else:
        PD.to_csv(path + name + '.csv', index=False, header=True)


def test_notears_linear_numpy(X,B_true):
    time_start = time.time()
    W_est = learning_dag(X = X, model = 'linear', method = 'notears')
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_notears_linear_torch(X,B_true):
    time_start = time.time()
    W_est = learning_dag(X = X, model = 'linear', method = 'notears', 
                        compute_lib = 'torch',device= 'cpu')
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_notears_linear_original(X,B_true):
    time_start = time.time()
    W_est = notears_linear(X, lambda1=0.1, loss_type='l2')
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_dagma_original(X,B_true):
    time_start = time.time()
    model = DagmaLinear(loss_type='l2')
    W_est = model.fit(X, lambda1=0.1)
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_dagma_numpy(X,B_true):
    time_start = time.time()
    W_est = learning_dag(X = X, model = 'linear', method = 'dagma')
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_dagma_torch(X,B_true):
    time_start = time.time()
    W_est = learning_dag(X = X, model = 'linear', method = 'dagma', 
                        compute_lib = 'torch', device= 'cpu')
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_topo_linear_original(X,B_true):
    n, d = X.shape
    time_start = time.time()
    topo_init = list(np.random.permutation(range(d)))
    model = TOPO_linear(regress= regress, score= score)
    size_small, size_large, no_large_search =set_sizes_linear(d, size_small= -1, size_large = -1, no_large_search = -1)
    W_est, _, _, _ = model.fit(X, topo = topo_init, no_large_search = no_large_search, size_small = size_small, size_large = size_large)
    W_est = threshold_W(W_est)
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_topo_linear_numpy(X,B_true):
    time_start = time.time()
    W_est = learning_dag(X = X, model = 'linear', method = 'topo')
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_notears_nonlinear_original(X,B_true):
    n, d = X.shape
    time_start = time.time()
    model = NotearsMLP(dims = [d, 40, 1])
    X = X.astype(np.float32)
    W_est = notears_nonlinear(model = model, X = X, lambda1=0.01, lambda2= 0.01)
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_notears_nonlinear_torch(X,B_true):
    time_start = time.time()
    X = X.astype(np.float32)
    W_est = learning_dag(X = X, model = 'nonlinear', method = 'notears', 
                        compute_lib = 'torch', reg = 'l1', general_options={'lambda1': 0.01, 'lambda2': 0.01})
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_dagma_nonlinear_original(X,B_true):
    n, d = X.shape
    time_start = time.time()
    X = X.astype(np.float32)
    model = DagmaNonlinear(DagmaMLP(dims = [d, 40, 1],bias=True))
    W_est = model.fit(X, lambda1=0.01, lambda2=0.01)
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_dagma_nonlinear_torch(X,B_true):
    time_start = time.time()
    X = X.astype(np.float32)
    W_est = learning_dag(X = X, model = 'nonlinear', method = 'dagma', 
                        compute_lib = 'torch')
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_topo_nonlinear_original(X,B_true):
    X = X.astype(np.float32)
    n, d = X.shape
    topo_init = list(np.random.permutation(range(d)))
    time_start = time.time()
    dims = [d, 40, 1]
    Topo_mlp = TopoMLP(dims = dims)
    model = TOPO_Nonlinear(X = X, model = Topo_mlp, num_iter=25,
                            lambda1 = 0.01, lambda2 = 0.01, loss_type='l2', opti='LBFGS', lr_decay= False)
    size_small, size_large, no_large_search =set_sizes_nonlinear(d, size_small= -1, size_large = -1, no_large_search = -1)
    W_est, _, _, _ = model.fit(topo = topo_init, no_large_search = no_large_search, size_small = size_small, size_large = size_large)
    W_est = threshold_W(W_est)
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime

def test_topo_nonlinear_torch(X,B_true):
    X = X.astype(np.float32)
    time_start = time.time()
    W_est = learning_dag(X = X, model = 'nonlinear', method = 'topo')
    time_end = time.time()
    runtime = round(time_end - time_start,3)
    accuracy = utils.count_accuracy(B_true = B_true, B_est= (W_est!=0))
    fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
    return fdr,tpr,fpr,shd, nnz, runtime



def main(args):
    import datetime
    from pathlib import Path
    dir_name = args.dir_name
    if dir_name:
        ppath = os.getcwd() + '/experiments/' + dir_name + '/'
    else:
        now = datetime.now()
        dir_name = now.strftime("%d_%m_%Y_%H_%M_%S")
        ppath = os.getcwd() + '/experiments/' + dir_name + '/'
    Path(ppath).mkdir(parents=True, exist_ok=True)
    
    seeds = args.seeds
    d = args.d
    n = args.n
    graph = args.graph
    k = args.k
    methods = args.methods
    model = args.model
    for seed in seeds:
        utils.set_random_seed(seed=seed)
        if model =='linear':
            sem = 'gauss'
            X, W_true, B_true = generate_linear_data(n,d,d*k,graph,sem,seed=seed)
        elif model == 'nonlinear':
            sem = 'mlp'
            X, B_true = generate_nonlinear_data(n,d,d*k,graph,sem,seed=seed)
        else:
            raise ValueError('Model not supported')
        
        if 'notears_linear_original' in methods:
            print('Testing Notears Linear Original')
            fdr,tpr,fpr,shd, nnz, runtime = test_notears_linear_original(X,B_true)
            results_dict = {'seed':seed,'method':'notears_linear_original','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'notears_linear_numpy' in methods:
            print('Testing Notears Linear Numpy')
            fdr,tpr,fpr,shd, nnz, runtime = test_notears_linear_numpy(X,B_true)
            results_dict = {'seed':seed, 'method':'notears_linear_numpy','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'notears_linear_torch' in methods:
            print('Testing Notears Linear Torch')
            fdr,tpr,fpr,shd, nnz, runtime = test_notears_linear_torch(X,B_true)
            results_dict = {'seed':seed, 'method':'notears_linear_torch','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'dagma_linear_original' in methods:
            print('Testing Dagma Linear Original')
            fdr,tpr,fpr,shd, nnz, runtime = test_dagma_original(X,B_true)
            results_dict = {'seed':seed, 'method':'dagma_linear_original','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'dagma_linear_numpy' in methods:
            print('Testing Dagma Linear Numpy')
            fdr,tpr,fpr,shd, nnz, runtime = test_dagma_numpy(X,B_true)
            results_dict = {'seed':seed, 'method':'dagma_linear_numpy','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'dagma_linear_torch' in methods:
            print('Testing Dagma Linear Torch')
            fdr,tpr,fpr,shd, nnz, runtime = test_dagma_torch(X,B_true)
            results_dict = {'seed':seed, 'method':'dagma_linear_torch','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'topo_linear_original' in methods:
            print('Testing Topo Linear Original')
            fdr,tpr,fpr,shd, nnz, runtime = test_topo_linear_original(X,B_true)
            results_dict = {'seed':seed, 'method':'topo_linear_original','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'topo_linear_numpy' in methods:
            print('Testing Topo Linear Numpy')
            fdr,tpr,fpr,shd, nnz, runtime = test_topo_linear_numpy(X,B_true)
            results_dict = {'seed':seed, 'method':'topo_linear_numpy','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'notears_nonlinear_original' in methods:
            print('Testing Notears Nonlinear Original')
            fdr,tpr,fpr,shd, nnz, runtime = test_notears_nonlinear_original(X,B_true)
            results_dict = {'seed':seed, 'method':'notears_nonlinear_original','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'notears_nonlinear_torch' in methods:
            print('Testing Notears Nonlinear Torch')
            fdr,tpr,fpr,shd, nnz, runtime = test_notears_nonlinear_torch(X,B_true)
            results_dict = {'seed':seed, 'method':'notears_nonlinear_torch','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'dagma_nonlinear_original' in methods:
            print('Testing Dagma Nonlinear Original')
            fdr,tpr,fpr,shd, nnz, runtime = test_dagma_nonlinear_original(X,B_true)
            results_dict = {'seed':seed, 'method':'dagma_nonlinear_original','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'dagma_nonlinear_torch' in methods:
            print('Testing Dagma Nonlinear Torch')
            fdr,tpr,fpr,shd, nnz, runtime = test_dagma_nonlinear_torch(X,B_true)
            results_dict = {'seed':seed, 'method':'dagma_nonlinear_torch','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)
        
        if 'topo_nonlinear_original' in methods:
            print('Testing Topo Nonlinear Original')
            fdr,tpr,fpr,shd, nnz, runtime = test_topo_nonlinear_original(X,B_true)
            results_dict = {'seed':seed, 'method':'topo_nonlinear_original','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)

        if 'topo_nonlinear_torch' in methods:
            print('Testing Topo Nonlinear Torch')
            fdr,tpr,fpr,shd, nnz, runtime = test_topo_nonlinear_torch(X,B_true)
            results_dict = {'seed':seed, 'method':'topo_nonlinear_torch','d':d,'n':n,'graph':graph,'k':k, 'sem': sem,'fdr':fdr,'tpr':tpr,'fpr':fpr,'nnz':nnz, 'shd':shd,'runtime':runtime}
            save_results(results_dict,ppath)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run experiments')
    parser.add_argument('--dir_name', type=str, default=None, help='Directory name to save results')
    parser.add_argument('--seeds', nargs='+', type=int, help='Random seeds')
    parser.add_argument('--d', type=int, default=10, help='Number of nodes')
    parser.add_argument('--n', type=int, default=1000, help='Number of samples')
    parser.add_argument('--graph', type=str, default='ER', help='Graph type')
    parser.add_argument('--k', type=int, default=1, help='Number of parents')
    parser.add_argument('--model', type=str, default='linear', help='Model type')
    parser.add_argument('--methods', nargs='+', choices=['notears_linear_numpy','notears_linear_torch','notears_linear_original',
                                                         'dagma_linear_numpy','dagma_linear_torch','dagma_linear_original',
                                                         'topo_linear_numpy','topo_linear_original',
                                                         'notears_nonlinear_original','notears_nonlinear_torch',
                                                         'dagma_nonlinear_original','dagma_nonlinear_torch',
                                                         'topo_nonlinear_original','topo_nonlinear_torch'], 
                        required= True, help='Methods to test')
    args = parser.parse_args()
    main(args)





