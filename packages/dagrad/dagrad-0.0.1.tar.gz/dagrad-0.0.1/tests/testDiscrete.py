import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dagrad.daglearner import learning_dag
import unittest
import numpy as np
import time
from dagrad.utils import utils
from test_cdt import shd_cpdag
def generate_linear_data(n,d,s0,graph_type,sem_type,seed=111):
        utils.set_random_seed(seed=seed)
        B_true = utils.simulate_dag(d, s0, graph_type)
        W_true = utils.simulate_parameter(B_true)
        X = utils.simulate_linear_sem(W_true, n, sem_type)
        return X, W_true, B_true

    
if __name__ == '__main__':
    n, d, s0, graph_type, sem_type = 10000, 5, 10, 'ER', 'logistic'
    X, W_true, B_true = generate_linear_data(n,d,s0,graph_type,sem_type)
    verbose = True

    start = time.time()

    W_est = learning_dag(X = X, model = 'nonlinear', method = 'notears', loss_fn = 'logistic', optimizer = 'lbfgs',
                             method_options={'verbose': verbose}, general_options={'lambda1':0.0, 'lambda2':0,'w_threshold':0.0})
    print(W_est)
    print(shd_cpdag(W_true, utils.threshold_W(W_est)))
    end = time.time()

    
        