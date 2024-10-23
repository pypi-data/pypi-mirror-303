import sys
import os
from dagrad.daglearner import dagrad
import numpy as np
import time
from dagrad.utils import utils
from notears.linear import notears_linear
from notears.nonlinear import notears_nonlinear, NotearsMLP
from dagma.linear import DagmaLinear
from dagma.nonlinear import DagmaNonlinear,DagmaMLP
# from dagrad.utils.topo_utils import set_sizes_linear, set_sizes_nonlinear
# from topo.topo_linear import TOPO_linear, regress, score
# from topo.topo_utils import threshold_W
# from topo.topo_nonlinear import TopoMLP, TOPO_Nonlinear

class Benchmarking():
    @staticmethod
    def generate_linear_data(n,d,s0,graph_type,sem_type,seed=1234):
        utils.set_random_seed(seed=seed)
        B_true = utils.simulate_dag(d, s0, graph_type)
        W_true = utils.simulate_parameter(B_true)
        X = utils.simulate_linear_sem(W_true, n, sem_type)
        return X, W_true, B_true
    @staticmethod
    def generate_nonlinear_data(n,d,s0,graph_type,sem_type,seed=1234):
        utils.set_random_seed(seed=seed)
        B_true = utils.simulate_dag(d, s0, graph_type)
        X = utils.simulate_nonlinear_sem(B_true, n, sem_type)
        return X, B_true
    
    def NOTEARSLinear(self):
        ns = [1000]
        ds = [10]
        ks = [4]
        graph_types = ['ER']
        sem_types = ['gauss']
        rep = 1
        for n in ns:
            for d in ds:
                for k in ks:
                    for graph_type in graph_types:
                        for sem_type in sem_types:
                            for i in range(rep):
                            
                                print('-'*50)
                                print(f"We are testing Linear SEM,  n={n}, d={d}, k={k}, graph={graph_type}, sem_type={sem_type} , {i}-th repetition\n")
                                X, W_true, B_true = self.generate_linear_data(n,d,d*k,graph_type,sem_type=sem_type)

                                time_start = time.time()
                                W_est = dagrad(X = X, model = 'linear', method = 'notears', general_options={'lambda1': 0.15}, 
                                                     method_options={'verbose':True})
                                time_end = time.time()
                                acc = utils.count_accuracy(B_true, W_est != 0)
                                
                                print('Accuracy for Notears (numpy) with New Implementation:', acc)
                                print('Time taken for Notears (numpy): ', time_end - time_start)
                                
                                time_start = time.time()
                                W_est = dagrad(X = X, model = 'linear', method = 'notears', 
                                                    compute_lib = 'torch', device = 'cpu', general_options={'lambda1': 0.15},
                                                    method_options={'verbose':True})
                                time_end = time.time()
                                print('Accuracy for Notears (torch) with New Implementation:', acc)
                                print('Time taken for Notears (torch cpu): ', time_end - time_start)

                                time_start = time.time()
                                W_est = notears_linear(X, lambda1=0.1, loss_type='l2')
                                time_end = time.time()
                                acc = utils.count_accuracy(B_true, W_est != 0)
                                print('Accuracy for Notears (numpy) with Original Implementation:', acc)
                                print('Time taken for Notears (numpy): ', time_end - time_start)
                                print('\n')

    def NOTEARSNonLinear(self):
        ns = [1000]
        ds = [10, 20]
        ks = [1, 2]
        graph_types = ['ER']
        sem_types = ['mlp'] # min
        rep = 1
        for n in ns:
            for d in ds:
                for k in ks:
                    for graph_type in graph_types:
                        for sem_type in sem_types:
                            for i in range(rep):
                                model = NotearsMLP(dims = [d, 40, 1])
                                print('-'*50)
                                print(f"We are testing Nonlinear SEM, n={n}, d={d}, k={k}, graph={graph_type}, sem_type={sem_type} , {i}-th repetition\n")
                                X, B_true = self.generate_nonlinear_data(n,d,d*k,graph_type,sem_type=sem_type)
                                X = X.astype(np.float32)

                                # time_start = time.time()
                                # W_est = dagrad(X = X, model = 'nonlinear', method = 'notears', reg = 'l1', general_options={'lambda1': 0.01, 'lambda2': 0.01})
                                # time_end = time.time()
                                # acc = utils.count_accuracy(B_true, W_est != 0)
                                
                                # print('Accuracy for Notears with New Implementation:', acc)
                                # print('Time taken for Notears: ', time_end - time_start)

                                X = X.astype(np.float32)
                                time_start = time.time()
                                W_est = notears_nonlinear(model, X, lambda1=0.01, lambda2= 0.01)
                                time_end = time.time()
                                acc = utils.count_accuracy(B_true, W_est != 0)
                                print('Accuracy for Notears (numpy) with Original Implementation:', acc)
                                print('Time taken for Notears (numpy): ', time_end - time_start)
                                print('\n')

    def DAGMALinear(self):
        ns = [1000]
        ds = [20]
        ks = [4]
        graph_types = ['ER']
        sem_types = ['gauss']
        rep = 1
        for n in ns:
            for d in ds:
                for k in ks:
                    for graph_type in graph_types:
                        for sem_type in sem_types:
                            for i in range(rep):
                            
                                print('-'*50)
                                print(f"We are testing Linear SEM,  n={n}, d={d}, k={k}, graph={graph_type}, sem_type={sem_type} , {i}-th repetition\n")
                                X, W_true, B_true = self.generate_linear_data(n,d,d*k,graph_type,sem_type=sem_type)

                                time_start = time.time()
                                W_est = dagrad(X = X, model = 'linear', method = 'dagma', method_options={'verbose':False})
                                time_end = time.time()
                                acc = utils.count_accuracy(B_true, W_est != 0)
                                
                                print('Accuracy for Dagma (numpy) with New Implementation:', acc)
                                print('Time taken for Dagma (numpy): ', time_end - time_start)
                                
                                time_start = time.time()
                                W_est = dagrad(X = X, model = 'linear', method = 'dagma', 
                                                    compute_lib = 'torch', device = 'cpu', method_options={'verbose':True})
                                time_end = time.time()
                                print('Accuracy for Dagma (torch) with New Implementation:', acc)
                                print('Time taken for Dagma (torch cpu): ', time_end - time_start)

                                time_start = time.time()
                                model = DagmaLinear(loss_type='l2')
                                W_est = model.fit(X, lambda1=0.1)
                                time_end = time.time()
                                acc = utils.count_accuracy(B_true, W_est != 0)
                                print('Accuracy for Dagma (numpy) with Original Implementation:', acc)
                                print('Time taken for Dagma (numpy): ', time_end - time_start)
                                print('\n')

    def DAGMANonLinear(self):
        ns = [1000]
        ds = [10, 20]
        ks = [1, 2]
        graph_types = ['ER']
        sem_types = ['mlp']
        rep = 1

        for n in ns:
            for d in ds:
                for k in ks:
                    for graph_type in graph_types:
                        for sem_type in sem_types:
                            for i in range(rep):
                                
                                print('-'*50)
                                print(f"We are testing Nonlinear SEM, n={n}, d={d}, k={k}, graph={graph_type}, sem_type={sem_type} , {i}-th repetition\n")
                                X, B_true = self.generate_nonlinear_data(n,d,d*k,graph_type,sem_type=sem_type)
                                X = X.astype(np.float32)

                                # time_start = time.time()
                                # W_est = dagrad(X = X, model = 'nonlinear', method = 'dagma', reg = 'l1', general_options={'lambda1': 0.01, 'lambda2': 0.01})
                                # time_end = time.time()
                                # acc = utils.count_accuracy(B_true, W_est != 0)
                                # print('Accuracy for Dagma with New Implementation:', acc)
                                # print('Time taken for Dagma: ', time_end - time_start)

                                X = X.astype(np.float32)
                                time_start = time.time()
                                model = DagmaNonlinear(DagmaMLP(dims = [d, 40, 1],bias=True))
                                W_est = model.fit(X, lambda1=0.01, lambda2=0.01)
                                time_end = time.time()
                                acc = utils.count_accuracy(B_true, W_est != 0)
                                print('Accuracy for Dagma (numpy) with Original Implementation:', acc)
                                print('Time taken for Dagma (numpy): ', time_end - time_start)
                                print('\n')

    def TOPOLinear(self):
        ns = [1000]
        ds = [10, 20]
        ks = [1, 2, 4]
        graph_types = ['ER', 'SF']
        sem_types = ['gauss']
        rep = 1
        for n in ns:
            for d in ds:
                for k in ks:
                    for graph_type in graph_types:
                        for sem_type in sem_types:
                            for i in range(rep):
                            
                                print('-'*50)
                                print(f"We are testing Linear SEM,  n={n}, d={d}, k={k}, graph={graph_type}, sem_type={sem_type} , {i}-th repetition\n")
                                X, W_true, B_true = self.generate_linear_data(n,d,d*k,graph_type,sem_type=sem_type)

                                topo_init = list(np.random.permutation(range(d)))

                                time_start = time.time()
                                W_est = dagrad(X = X, model = 'linear', method = 'topo', method_options={'topo': topo_init})
                                time_end = time.time()
                                acc = utils.count_accuracy(B_true, W_est != 0)
                                print('Accuracy for Topo (numpy) with New Implementation:', acc)
                                print('Time taken for Topo (numpy): ', time_end - time_start)
                                

                                # time_start = time.time()
                                # model = TOPO_linear(regress= regress, score= score)
                                # size_small, size_large, no_large_search =set_sizes_linear(d, size_small= -1, size_large = -1, no_large_search = -1)
                                # W_est, _, _, _ = model.fit(X, topo = topo_init, no_large_search = no_large_search, size_small = size_small, size_large = size_large)
                                # W_est = threshold_W(W_est)
                                # time_end = time.time()
                                # acc = utils.count_accuracy(B_true, W_est != 0)
                                # print('Accuracy for Topo (numpy) with Original Implementation:', acc)
                                # print('Time taken for Topo (numpy): ', time_end - time_start)
                                print('\n')


    def TOPONonLinear(self):
        ns = [1000]
        ds = [10, 20]
        ks = [1, 2]
        graph_types = ['ER']
        sem_types = ['mlp']
        rep = 1
        for n in ns:
            for d in ds:
                for k in ks:
                    for graph_type in graph_types:
                        for sem_type in sem_types:
                            for i in range(rep):
                                print('-'*50)
                                dims = [d, 40, 1]
                                print(f"We are testing Nonlinear SEM, n={n}, d={d}, k={k}, graph={graph_type}, sem_type={sem_type} , {i}-th repetition\n")
                                X, B_true = self.generate_nonlinear_data(n,d,d*k,graph_type,sem_type=sem_type)
                                X = X.astype(np.float32)

                                topo_init = list(np.random.permutation(range(d)))

                                time_start = time.time()
                                W_est = dagrad(X = X, model = 'nonlinear', method = 'topo', 
                                                     method_options={'topo': topo_init, 'dims': dims, 'verbose': True},
                                                     general_options={'lambda1': 0.01, 'lambda2': 0.01})
                                time_end = time.time()
                                acc = utils.count_accuracy(B_true, W_est != 0)
                                print('Accuracy for Topo with New Implementation:', acc)
                                print('Time taken for Topo: ', time_end - time_start)

                                # X = X.astype(np.float32)
                                # time_start = time.time()
                                # Topo_mlp = TopoMLP(dims = dims)
                                # model = TOPO_Nonlinear(X = X, model = Topo_mlp, num_iter=25,
                                #                        lambda1 = 0.01, lambda2 = 0.01, loss_type='l2', opti='LBFGS', lr_decay= False)
                                # size_small, size_large, no_large_search =set_sizes_nonlinear(d, size_small= -1, size_large = -1, no_large_search = -1)
                                # W_est, _, _, _ = model.fit(topo = topo_init, no_large_search = no_large_search, size_small = size_small, size_large = size_large)
                                # W_est = threshold_W(W_est)
                                # time_end = time.time()
                                # acc = utils.count_accuracy(B_true, W_est != 0)
                                # print('Accuracy for Topo with Original Implementation:', acc)
                                # print('Time taken for Topo: ', time_end - time_start)
                                print('\n')

if __name__ == '__main__':
    benchmark = Benchmarking()
    benchmark.NOTEARSLinear()
    # benchmark.NOTEARSNonLinear()
    # benchmark.DAGMALinear()
    # benchmark.DAGMANonLinear()
    # benchmark.TOPOLinear()
    # benchmark.TOPONonLinear()
    



                                
