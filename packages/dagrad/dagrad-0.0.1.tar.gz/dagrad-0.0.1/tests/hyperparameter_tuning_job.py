import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dagrad.daglearner import learning_dag
import numpy as np
import time
from dagrad.utils import utils
from dagrad.utils.general_utils import set_functions
from dagrad.utils.configure import loss_functions

from notears.notears.linear import notears_linear
from notears.notears.nonlinear import notears_nonlinear, NotearsMLP
from dagma.linear import DagmaLinear
from dagma.nonlinear import DagmaNonlinear,DagmaMLP
from dagrad.utils.topo_utils import set_sizes_linear, set_sizes_nonlinear
from topo.topo_linear import TOPO_linear, regress, score
from topo.topo_utils import threshold_W
from topo.topo_nonlinear import TopoMLP, TOPO_Nonlinear
import pandas as pd
# os.environ['R_HOME'] = '/Library/Frameworks/R.framework/Resources'  # Correct path to R
# os.environ['R_USER'] = "/Users/duntrain/Library/R/arm64/4.4/library" 
# from cdt.metrics import SHD_CPDAG

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

def generate_linear_uneq_data(n,d,s0,graph_type,sem_type,seed=1234):
        std_low, std_high = 0.1, 0.5
        utils.set_random_seed(seed=seed)
        B_true = utils.simulate_dag(d, s0, graph_type)
        W_true = utils.simulate_parameter(B_true)
        std = np.random.uniform(std_low, std_high, d)
        Omega =np.diag(std**2)
        X = utils.simulate_linear_sem(W_true, n, sem_type, std)
        return X, W_true, Omega

def generate_nonlinear_data(n,d,s0,graph_type,sem_type,seed=1234):
        utils.set_random_seed(seed=seed)
        B_true = utils.simulate_dag(d, s0, graph_type)
        X = utils.simulate_nonlinear_sem(B_true, n, sem_type)
        return X, B_true

def generate_linear_eq_data(n,d,s0,graph_type,sem_type,seed=1234):
        utils.set_random_seed(seed=seed)
        B_true = utils.simulate_dag(d, s0, graph_type)
        W_true = utils.simulate_parameter(B_true)
        X = utils.simulate_linear_sem(W_true, n, sem_type)
        return X, W_true, B_true

def save_results(results, 
                 selection_method, 
                 method,
                 reg, 
                 reg_paras, 
                 seed, 
                 n, 
                 d, 
                 k,
                 graph,
                 model,
                 sem, 
                 eq,
                 path):
    name = f"{d}_{k}_{graph}_{model}_{sem}"
    columns = ['seed','method','n','d','k','graph','model','sem','eq','selection_method','reg','lambda1','gamma','err','shd']
    PD = pd.DataFrame(columns = columns)

    if reg == 'l1' and selection_method == 'cv':
        lambda1s = reg_paras
        Err_list = results
        for lambda1, err in zip(lambda1s, Err_list):
            PD.loc[len(PD.index)] = [seed,method, n,d,k,graph,model,sem,eq,selection_method,reg,lambda1,-1,err,-1]
    
    if reg == 'l1' and selection_method == 'grid':
        lambda1s = reg_paras
        SHD_list = results
        for lambda1, shd in zip(lambda1s, SHD_list):
            PD.loc[len(PD.index)] = [seed,method, n,d,k,graph,model,sem,eq,selection_method,reg,lambda1,-1,-1,shd]
    
    if reg == 'l1' and selection_method in ['decay','decay_plus']:
        lambda1s = reg_paras.copy()
        lambda1s.sort(reverse = True)
        Err_list = results
        for lambda1, err in zip(lambda1s, Err_list):
            PD.loc[len(PD.index)] = [seed,method, n,d,k,graph,model,sem,eq,selection_method,reg,lambda1,-1,err,-1]
    
    if reg == 'mcp' and selection_method == 'cv':
        lambda1s, gammas = reg_paras[0],reg_paras[1]
        reg_space = [[gamma, lambda1] for gamma in gammas for lambda1 in lambda1s]
        Err_list = results
        for [gamma, lambda1], err in zip(reg_space, Err_list):
            PD.loc[len(PD.index)] = [seed,method, n,d,k,graph,model,sem,eq, selection_method,reg,lambda1,gamma,err,-1]
    
    if reg == 'mcp' and selection_method == 'grid':
        lambda1s, gammas = reg_paras[0],reg_paras[1]
        reg_space = [[gamma, lambda1] for gamma in gammas for lambda1 in lambda1s]
        SHD_list = results
        for [gamma, lambda1], shd in zip(reg_space, SHD_list):
            PD.loc[len(PD.index)] = [seed,method,n,d,k,graph,model,sem,eq, selection_method,reg,lambda1,gamma,-1,shd]
    
    if reg == 'mcp' and selection_method in ['decay','decay_plus']:
        lambda1s, gammas = reg_paras.copy()
        lambda1s.sort(reverse = True)
        gammas.sort(reverse = True)
        Err_list = results
        for gamma, lambda1, err in zip(gammas, lambda1s, Err_list):
            PD.loc[len(PD.index)] = [seed,method,n,d,k,graph,model,sem,eq, selection_method,reg,lambda1,gamma,err,-1]

    if os.path.isfile(path + name + '.csv'):
        PD.to_csv(path + name + '.csv', mode='a', index=False, header=False)
    else:
        PD.to_csv(path + name + '.csv', index=False, header=True)


def cross_validation(X, K, reg_paras, model = 'linear', method = 'notears',reg = 'l1', eq = True):
    if eq:
        loss_fn = 'l2'
    else:
        loss_fn = 'logll'

    _loss = set_functions(loss_fn, loss_functions)
    # split data into K folds
    n = X.shape[0]
    # indices = np.arange(n)
    # np.random.shuffle(indices)
    indices =  np.arange(n)
    fold_size = n//K
    folds = []
    for k in range(K):
        if k == K-1:
            folds.append(indices[k*fold_size:])
        else:
            folds.append(indices[k*fold_size:(k+1)*fold_size])
    

    Err_list = []
    if reg == 'l1':
        lambda1s = reg_paras
        for lambda1 in lambda1s:
            Err_total = 0
            for k in range(K):
                test_indices = folds[k]
                train_indices = np.concatenate([folds[j] for j in range(K) if j != k])
                X_train = X[train_indices]
                X_test = X[test_indices]
                # fit model
                if eq:
                    W_est = learning_dag(X = X_train, 
                                        model = model, 
                                        method= method, 
                                        reg = reg, 
                                        loss_fn = loss_fn,
                                        general_options={'lambda1':lambda1, 'w_threshold':0.0})
                    
                    
                else:
                    W_est = learning_dag(X, 
                                     method = 'dagma', 
                                     model = model, 
                                     loss_fn = 'l2',
                                     general_options={'w_threshold':0.0})
                    W_est =  learning_dag(X = X_train, 
                                        model = model, 
                                        method= method, 
                                        reg = reg, 
                                        loss_fn = loss_fn,
                                        general_options={'lambda1':lambda1, 'initialization':W_est, 'w_threshold':0.0},
                                        method_options = {'mu_init':0.0001, 'T':4})
                Err, _ = _loss(W = W_est, X = X_test)
                # Err = 0.5 * ((X_test - X_test@W_est)**2).sum()
                Err_total += Err
            Err_average = Err_total / K
            Err_list.append(Err_average)


    elif reg == 'mcp':
        lambda1s, gammas = reg_paras[0], reg_paras[1]
        reg_space = [[gamma, lambda1] for gamma in gammas for lambda1 in lambda1s]
        for gamma, lambda1 in reg_space:
            Err_total = 0
            for k in range(K):
                test_indices = folds[k]
                train_indices = np.concatenate([folds[j] for j in range(K) if j != k])
                X_train = X[train_indices]
                X_test = X[test_indices]
                # fit model
                if eq:
                    W_est = learning_dag(X = X_train, 
                                        model = model, 
                                        method= method, 
                                        reg = reg,  
                                        loss_fn = loss_fn,
                                        general_options={'lambda1':lambda1, 'gamma':gamma, 'w_threshold':0.0})
                else:
                    W_est = learning_dag(X, 
                                     method = 'dagma', 
                                     model = model, 
                                     loss_fn = 'l2',
                                     general_options={'w_threshold':0.0})
                    W_est =  learning_dag(X = X_train, 
                                        model = model, 
                                        method= method, 
                                        reg = reg, 
                                        loss_fn = loss_fn,
                                        general_options={'lambda1':lambda1, 'gamma':gamma, 'initialization':W_est, 'w_threshold':0.0},
                                        method_options = {'mu_init':0.0001, 'T':4})

                # evaluate model
                Err, _ = _loss(W = W_est, X = X_test)
                #Err = 0.5 * ((X_test - X_test@W_est)**2).sum()
                Err_total += Err
            Err_average = Err_total / K
            Err_list.append(Err_average)
    return Err_list

        
def grid_search(X, reg_paras, W_true, model = 'linear', method = 'notears',reg = 'l1', eq = True):
    if eq:
        loss_fn = 'l2'
    else:
        loss_fn = 'logll'
    # _loss = set_functions(loss_fn, loss_functions)

    SHD_list = []
    if reg == 'l1':
        lambda1s = reg_paras
        for lambda1 in lambda1s:
            if eq:
                # fit model
                W_est = learning_dag(X = X, 
                                    model = model, 
                                    method= method, 
                                    loss_fn = loss_fn,
                                    reg = reg, 
                                    general_options={'lambda1':lambda1})
                if not utils.is_dag(W_est):
                    W_est = utils.threshold_till_dag(W_est) 
                # evaluate model
                
                accuracy = utils.count_accuracy(B_true = (W_true!=0), B_est= (W_est!=0))
                fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
                SHD_list.append(shd)
            else:
                # working with logll, first use run 'dagma' with 'l2' to get initialization
                W_est = learning_dag(X, 
                                     method = 'dagma', 
                                     model = model, 
                                     loss_fn = 'l2',
                                     general_options={'w_threshold':0.0})
                # I don't use notears, since it use different method parameter
                # if we add 'notears', it means we need another paramters
                W_est =  learning_dag(X, method = 'dagma', 
                                        model = model, 
                                        reg = reg, 
                                        loss_fn = loss_fn, 
                                        optimizer = 'adam',
                                        general_options = {'lambda1':lambda1, 'initialization': W_est},
                                        method_options = {'mu_init':0.0001, 'T':4})

                if not utils.is_dag(W_est):
                    W_est = utils.threshold_till_dag(W_est)
                SHD_list.append(shd_cpdag(W_true, W_est))

    elif reg == 'mcp':
        lambda1s, gammas = reg_paras[0], reg_paras[1]
        reg_space = [[gamma, lambda1] for gamma in gammas for lambda1 in lambda1s]
        for gamma, lambda1 in reg_space:
            if eq:
            # fit model
                W_est = learning_dag(X = X, 
                                    model = model, 
                                    method= method, 
                                    reg = reg, 
                                    loss_fn= loss_fn,
                                    general_options={'lambda1':lambda1, 'gamma':gamma})
                if not utils.is_dag(W_est):
                    W_est = utils.threshold_till_dag(W_est) 
                # evaluate model
                accuracy = utils.count_accuracy(B_true = (W_true!=0), B_est= (W_est!=0))
                fdr,tpr,fpr,shd,nnz = accuracy['fdr'],accuracy['tpr'],accuracy['fpr'],accuracy['shd'],accuracy['nnz']
                SHD_list.append(shd)  
            else:
                # working with logll, first use run 'dagma' with 'l2' to get initialization
                W_est = learning_dag(X, 
                                     method = 'dagma', 
                                     model = model, 
                                     loss_fn = 'l2',
                                     general_options={'w_threshold':0.0})
                # I don't use notears, since it use different method parameter
                # if we add 'notears', it means we need another paramters
                W_est =  learning_dag(X, method = 'dagma', 
                model = model, 
                reg = reg, 
                loss_fn = loss_fn, 
                optimizer = 'adam',
                general_options = {'lambda1':lambda1, 'gamma':gamma, 'initialization': W_est},
                method_options = {'mu_init':0.0001, 'T':4})

                if not utils.is_dag(W_est):
                    W_est = utils.threshold_till_dag(W_est)
                SHD_list.append(shd_cpdag(W_true, W_est))



    return SHD_list

def decay_search(X, reg_paras, model, method = 'notears',reg = 'l1', eq = True):
    # only consider linear model, but will extend to nonlinear model in the future
    if eq:
        loss_fn = 'l2'
    else:
        loss_fn = 'logll'
    _loss = set_functions(loss_fn, loss_functions)
    
    n, d = X.shape
    Err_list = []
    
    if reg == 'l1':
        lambda1s = reg_paras.copy()
        lambda1s.sort(reverse = True)
        if eq:
            W_est = np.zeros((d,d))
            for lambda1 in lambda1s:
                # fit model
                W_est = learning_dag(X = X, 
                                    model = model, 
                                    method= method, 
                                    reg = reg, 
                                    loss_fn= loss_fn,
                                    general_options={'lambda1':lambda1, 'initialization':W_est, 'w_threshold':0.0})
                # evaluate model
                Err, _ = _loss(W = W_est, X = X)
                # Err = 0.5/ X.shape[0] * ((X - X@W_est)**2).sum()
                Err_list.append(Err)
        else:
            # get initialization
            W_est = learning_dag(X, 
                                method = 'dagma', 
                                model = model, 
                                loss_fn = 'l2',
                                general_options={'w_threshold':0.0})
            

            for lambda1 in lambda1s:
                W_est = learning_dag(X = X, model = model, 
                                    method= method, 
                                    reg = reg, 
                                    loss_fn= loss_fn,
                                    general_options={'lambda1':lambda1, 'initialization':W_est, 'w_threshold':0.0})
                # evaluate model
                Err, _ = _loss(W = W_est, X = X)
                Err_list.append(Err)


    elif reg == 'mcp':
        reg_paras_= reg_paras.copy()
        lambda1s, gammas = reg_paras_[0],reg_paras_[1]
        lambda1s.sort(reverse = True)
        gammas.sort(reverse = True)
        if eq:
            W_est = np.zeros((d,d))
            for gamma, lambda1 in zip(gammas, lambda1s):
                # fit model
                W_est = learning_dag(X = X, 
                                    model = model, 
                                    method= method, 
                                    reg = reg, 
                                    loss_fn= loss_fn,
                                    general_options={'lambda1':lambda1, 'gamma':gamma, 'initialization':W_est, 'w_threshold':0.0})
                # evaluate model
                Err, _ = _loss(W = W_est, X = X)
                # Err = 0.5/ X.shape[0] * ((X - X@W_est)**2).sum()
                Err_list.append(Err)
        else:
            W_est = learning_dag(X, 
                                method = 'dagma', 
                                model = model, 
                                loss_fn = 'l2',
                                general_options={'w_threshold':0.0})
            for gamma, lambda1 in zip(gammas, lambda1s):
                W_est = learning_dag(X = X, model = model, 
                                    method= method, 
                                    reg = reg, 
                                    loss_fn= loss_fn,
                                    general_options={'lambda1':lambda1, 'gamma':gamma, 'initialization':W_est, 'w_threshold':0.0})
                # evaluate model
                Err, _ = _loss(W = W_est, X = X)
                Err_list.append(Err)
    
    return Err_list

def decay_search_plus(X, reg_paras, model, K = 5, method = 'notears', reg = 'l1', eq = True):
    if eq:
        loss_fn = 'l2'
    else:
        loss_fn = 'logll'
    _loss = set_functions(loss_fn, loss_functions)
    
    n, d = X.shape
    indices = np.arange(n)
    fold_size = n//K
    folds = []
    for k in range(K):
        if k == K-1:
            folds.append(indices[k*fold_size:])
        else:
            folds.append(indices[k*fold_size:(k+1)*fold_size])
    
    if reg == 'l1':
        Err_list = [0]*len(reg_paras)
        lambda1s = reg_paras.copy()
        lambda1s.sort(reverse = True)

        for k in range(K):
            test_indices = folds[k]
            training_indices = np.concatenate([folds[j] for j in range(K) if j != k])
            X_train = X[training_indices]
            X_test = X[test_indices]
            if eq:
                W_est = np.zeros((d,d))
                for idx, lambda1 in enumerate(lambda1s):
                    W_est = learning_dag(X = X_train, 
                                        model = model, 
                                        method= method, 
                                        reg = reg, 
                                        loss_fn= loss_fn,
                                        general_options={'lambda1':lambda1, 'initialization':W_est, 'w_threshold':0.0})
                    Err, _ = _loss(W = W_est, X = X_test)
                    # Err = 0.5 * ((X_test - X_test@W_est)**2).sum()
                    Err_list[idx] += Err
            else:
                W_est = learning_dag(X, 
                                method = 'dagma', 
                                model = model, 
                                loss_fn = 'l2',
                                general_options={'w_threshold':0.0})
                for idx, lambda1 in enumerate(lambda1s):
                    W_est = learning_dag(X = X_train, 
                                        model = model, 
                                        method= method, 
                                        reg = reg, 
                                        loss_fn= loss_fn,
                                        general_options={'lambda1':lambda1, 'initialization':W_est, 'w_threshold':0.0},
                                        method_options={'mu_init':0.0001, 'T':4})
                    Err, _ = _loss(W = W_est, X = X_test)
                    Err_list[idx] += Err
    else:
        Err_list = [0]*len(reg_paras[0])

        reg_paras_= reg_paras.copy()
        lambda1s, gammas = reg_paras_[0],reg_paras_[1]
        lambda1s.sort(reverse = True)
        gammas.sort(reverse = True)
        
        for k in range(K):
            test_indices = folds[k]
            training_indices = np.concatenate([folds[j] for j in range(K) if j != k])
            X_train = X[training_indices]
            X_test = X[test_indices]
            if eq:
                W_est = np.zeros((d,d))
                for idx, (gamma, lambda1) in enumerate(zip(gammas, lambda1s)):
                    W_est = learning_dag(X = X_train, 
                                        model = model, 
                                        method= method, 
                                        reg = reg, 
                                        loss_fn= loss_fn,
                                        general_options={'lambda1':lambda1, 'gamma':gamma, 'initialization':W_est, 'w_threshold':0.0})

                    # Err = 0.5 * ((X_test - X_test@W_est)**2).sum()
                    Err, _ = _loss(W = W_est, X = X_test)
                    Err_list[idx] += Err
            else:
                W_est = learning_dag(X, 
                                method = 'dagma', 
                                model = model, 
                                loss_fn = 'l2',
                                general_options={'w_threshold':0.0})
                for idx, (gamma, lambda1) in enumerate(zip(gammas, lambda1s)):
                    W_est = learning_dag(X = X_train, 
                                        model = model, 
                                        method= method, 
                                        reg = reg, 
                                        loss_fn= loss_fn,
                                        general_options={'lambda1':lambda1, 'gamma':gamma, 'initialization':W_est, 'w_threshold':0.0})
                    Err, _ = _loss(W = W_est, X = X_test)
                    Err_list[idx] += Err

    Err_list = [Err/K for Err in Err_list]
    return Err_list

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
    method = args.method
    selection_methods = args.selection_methods
    model = args.model
    K = args.K
    reg_paras = eval(args.reg_paras)
    # reg_paras = [[0.0,0.05,0.1,0.2,0.3], [1.0,1.5,2.0,2.5,3.0]]
    reg = args.reg
    eq = args.eq
    eq = True if eq == 1 else False
    for seed in seeds:
        utils.set_random_seed(seed=seed)
        if model =='linear':
            sem = 'gauss'
            if eq:
                X, W_true, B_true = generate_linear_eq_data(n,d,d*k,graph,sem,seed=seed)
            else:
                X, W_true, Omega = generate_linear_uneq_data(n,d,d*k,graph,sem,seed=seed)
            # np.savetxt(f"{selection_methods[0]}_output.csv", X, delimiter=",", fmt="%.4f")
        elif model == 'nonlinear':
            sem = 'mlp'
            X, B_true = generate_nonlinear_data(n,d,d*k,graph,sem,seed=seed)
        else:
            raise ValueError('Model not supported')
        
        # reg_paras = [0.1, 0.01, 0.001, 0.0001] reg = 'l1' 

        if 'cv' in selection_methods:
            print(f'Cross validation, method: {method}')
            Err_list = cross_validation(X, K, reg_paras, model = model, method = method,reg = reg, eq = eq)
            save_results(results = Err_list, 
                         selection_method = 'cv', method = method,
                         reg = reg, 
                         reg_paras = reg_paras, 
                         seed = seed, n = n,
                         d = d, k = k,graph = graph, model = model,sem = sem, eq = eq, path = ppath)
            print(f'finish Cross validation, method: {method}')
        if 'grid' in selection_methods:
            print(f'Grid search, method: {method}')
            SHD_list = grid_search(X, reg_paras, W_true, model = model, method = method,reg = reg, eq = eq)
            save_results(results = SHD_list, 
                         selection_method = 'grid', method = method,
                         reg = reg, 
                         reg_paras = reg_paras, 
                         seed = seed, n = n,
                         d = d, k = k,graph = graph, model = model,sem = sem, eq = eq, path = ppath)
            print(f'finish Grid search, method: {method}')
        if 'decay' in selection_methods:
            print(f'Decay search, method: {method}')
            Err_list = decay_search(X, reg_paras, model = model, method = method,reg = reg, eq = eq)
            save_results(results = Err_list,
                            selection_method = 'decay', method = method,
                            reg = reg, 
                            reg_paras = reg_paras, 
                            seed = seed, n = n,
                            d = d, k = k,graph = graph, model = model,sem = sem, eq = eq, path = ppath)
            print(f'finish Decay search, method: {method}')
        if 'decay_plus' in selection_methods:
            print(f'Decay search plus, method: {method}')
            Err_list = decay_search_plus(X, reg_paras, model = model, K = K, method = method, reg = reg, eq = eq)
            save_results(results = Err_list,
                            selection_method = 'decay_plus', method = method,
                            reg = reg, 
                            reg_paras = reg_paras, 
                            seed = seed, n = n,
                            d = d, k = k,graph = graph, model = model,sem = sem, eq = eq, path = ppath)
            print(f'finish Decay search plus, method: {method}')
        
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Hyperparameter tuning')
    parser.add_argument('--dir_name', type=str, default='', help='Directory name to save results')
    parser.add_argument('--seeds', nargs='+', type = int, help='Random seeds')
    parser.add_argument('--d', type=int, default=20, help='Number of variables')
    parser.add_argument('--n', type=int, default=1000, help='Number of samples')
    parser.add_argument('--graph', type=str, default='ER', help='Graph type')
    parser.add_argument('--k', type=int, default=2, help='Average degree')
    parser.add_argument('--method', type=str, default='notears', help='Method')
    parser.add_argument('--selection_methods', nargs='+', choices=['cv','grid','decay','decay_plus'], help='Selection methods')
    parser.add_argument('--model', type=str, default='linear', help='Model')
    parser.add_argument('--K', type=int, default=5, help='Number of folds for cross validation')
    parser.add_argument('--reg_paras', type = str, help='Use string, Regularization parameters')
    parser.add_argument('--reg', type=str, default='l1', help='Regularization method')
    parser.add_argument('--eq', type=int, default=1)
    args = parser.parse_args()
    main(args)