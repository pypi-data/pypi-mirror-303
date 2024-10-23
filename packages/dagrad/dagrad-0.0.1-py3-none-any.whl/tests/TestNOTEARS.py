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
    
    def testNotearsGauss1(self):
        n, d, s0 = 1000, nnode, nedge # the ground truth is a DAG of 20 nodes and 20 edges in expectation
        graph_type, sem_type = 'ER', 'gauss'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'notears', method_options={'verbose': True})
        #W_est = learning_dag(X = X, model = 'linear', reg = 'mcp', method = 'notears',general_options={'lambda1': 0.2, 'gamma': 1.0}, method_options={'verbose': True})
        time_end = time.time()
        print('Working with linear Gaussian data')
        print('Time taken for Notears numpy: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for Notears: ', acc)

    def testNotearsGauss2(self):
        n, d, s0 = 1000, nnode, nedge # the ground truth is a DAG of 20 nodes and 20 edges in expectation
        graph_type, sem_type = 'ER', 'gauss'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'notears', 
                               compute_lib = 'torch', device = 'cpu', reg = 'mcp')
        # W_est = learning_dag(X = X, model = 'linear', method = 'notears', 
        #                        compute_lib = 'torch', device = 'cpu')
        time_end = time.time()
        print('Working with linear Gaussian data')
        print('Time taken for Notears torch cpu: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for Notears: ', acc)

    def testNotearsGauss3(self):
        n, d, s0 = 1000, nnode, nedge # the ground truth is a DAG of 20 nodes and 20 edges in expectation
        graph_type, sem_type = 'ER', 'gauss'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'notears',
                               compute_lib = 'torch', device = 'cuda')
        time_end = time.time()
        print('Working with linear Gaussian data')
        print('Time taken for Notears torch gpu: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for Notears: ', acc)

    def testNotearsLogistic1(self):
        n, d, s0 = 10000, nnode, nedge # the ground truth is a DAG of 20 nodes and 20 edges in expectation
        graph_type, sem_type = 'ER', 'logistic'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type,seed=2322)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'notears', loss_fn = 'logistic', method_options={'verbose': True})
        time_end = time.time()
        print('Working with linear logistic data')
        print('Time taken for Notears numpy: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for Notears numpy: ', acc)

    def testNotearsLogistic2(self):
        n, d, s0 = 1000, nnode, nedge # the ground truth is a DAG of 20 nodes and 40 edges in expectation
        graph_type, sem_type = 'ER', 'logistic'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'notears', loss_fn = 'logistic',
                               compute_lib = 'torch', device = 'cpu', method_options={'verbose': True})
        time_end = time.time()
        print('Working with linear logistic data')
        print('Time taken for Notears torch cpu: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for Notears: ', acc)
    
    def testNotearsLogistic3(self):
        n, d, s0 = 1000, nnode, nedge # the ground truth is a DAG of 20 nodes and 20 edges in expectation
        graph_type, sem_type = 'ER', 'logistic'
        X, W_true, B_true = self.generate_linear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'linear', method = 'notears', loss_fn = 'logistic',
                               compute_lib = 'torch', device = 'cuda')
        time_end = time.time()
        print('Working with linear logistic data')
        print('Time taken for Notears torch gpu: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for Notears: ', acc)
        
    def testNotearsMLP1(self):
        n, d, s0 = 1000, nnode, nedge
        graph_type, sem_type = 'ER', 'mlp'
        X, B_true = self.generate_nonlinear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'nonlinear', method = 'notears', reg = 'l1', method_options={'verbose': True})
        time_end = time.time()
        print('Working with nonlinear MLP data')
        print('Time taken for Notears torch cpu: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for Notears: ', acc)


    def testNotearsMLP2(self):
        n, d, s0 = 1000, nnode, nedge
        graph_type, sem_type = 'ER', 'mlp'
        X, B_true = self.generate_nonlinear_data(n,d,s0,graph_type,sem_type)
        time_start = time.time()
        W_est = learning_dag(X = X, model = 'nonlinear', method = 'notears',
                               compute_lib = 'torch', device = 'cuda')
        time_end = time.time()
        print('Working with nonlinear MLP data')
        print('Time taken for Notears torch gpu: ', time_end - time_start)
        acc = utils.count_accuracy(B_true, W_est != 0)
        print('Accuracy for Notears: ', acc)

if __name__ == '__main__':
    unittest.main()
