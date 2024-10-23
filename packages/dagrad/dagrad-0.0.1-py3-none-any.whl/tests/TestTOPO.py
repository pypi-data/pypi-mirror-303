import sys
import os
from dagrad.daglearner import learning_dag
import unittest
import numpy as np
import time
from dagrad.utils import utils

nnode = 5
nedge = 5

class TestLinear(unittest.TestCase):
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
    
    def testTopoGauss1(self):
        n, d, s0 = 1000, nnode, nedge # the ground truth is a DAG of 20 nodes and 20 edges in expectation
        graph_type, sem_type = 'ER', 'gauss'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'topo', method_options={'verbose': True})
        time_end = time.time()
        print('Working with linear Gaussian data')
        print('Time taken for topo sklearn: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for topo: ', acc)

    def testTopoGauss2(self):
        n, d, s0 = 1000, nnode, nedge # the ground truth is a DAG of 20 nodes and 20 edges in expectation
        graph_type, sem_type = 'ER', 'gauss'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'topo',
                               optimizer = 'lbfgs', method_options={'verbose': True})
        time_end = time.time()
        print('Working with linear Gaussian data')
        print('Time taken for topo lbfgs: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for topo lbfgs: ', acc)

    def testTopoLogistic1(self):
        n, d, s0 = 10000, 10, 20 # the ground truth is a DAG of 20 nodes and 20 edges in expectation
        graph_type, sem_type = 'ER', 'logistic'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'topo', loss_fn = 'logistic', 
                             method_options={'verbose': True, 'size_small': 30, 'size_large':45, 'no_large_search':3})
        time_end = time.time()
        print('Working with linear logistic data')
        print('Time taken for topo sklearn: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for topo sklearn: ', acc)

    def testTopoLogistic2(self):
        n, d, s0 = 10000, 10, 20 # the ground truth is a DAG of 20 nodes and 20 edges in expectation
        graph_type, sem_type = 'ER', 'logistic'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'topo', loss_fn = 'logistic',
                               optimizer = 'lbfgs', method_options={'verbose': True, 'size_small': 30, 'size_large':45, 'no_large_search':3})
        time_end = time.time()
        print('Working with linear logistic data')
        print('Time taken for topo using lbfgs: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for topo using lbfgs: ', acc)
        
    def testTopoMLP1(self):
        n, d, s0 = 1000, nnode, nedge
        graph_type, sem_type = 'ER', 'mlp'
        X, B_true = self.generate_nonlinear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'nonlinear', method = 'topo', method_options={'verbose': True}, general_options={'w_threshold': 0.6})
        time_end = time.time()
        print('Working with nonlinear MLP data')
        print('Time taken for topo torch cpu: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for topo torch cpu: ', acc)


if __name__ == '__main__':
    unittest.main()