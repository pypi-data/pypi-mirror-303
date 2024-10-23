import dagrad
from dagrad.daglearner import dagrad # dagrad is the main class for learning the structure of a DAG
from dagrad.utils import utils # utils is a module that contains some useful functions for generating data and measuring performance
from dagrad.utils.utils import generate_linear_data, generate_nonlinear_data

n, d, s0, graph_type, sem_type = 1000, 10, 10, 'ER', 'gauss' # Define the parameters of the data
X, W_true, B_true = generate_linear_data(n,d,s0,graph_type,sem_type) # Generate the data
model = 'linear' # Define the model
W_notears = dagrad(X, model = model, method = 'notears') # Learn the structure of the DAG using Notears
W_dagma = dagrad(X, model = model, method = 'dagma') # Learn the structure of the DAG using Dagma
W_topo = dagrad(X, model = model, method = 'topo') # Learn the structure of the DAG using Topo
print(f"Linear Model")
print(f"data size: {n}, graph type: {graph_type}, sem type: {sem_type}")

acc_notears = utils.count_accuracy(B_true, W_notears != 0) # Measure the accuracy of the learned structure using Notears
print('Accuracy of Notears:', acc_notears)

acc_dagma = utils.count_accuracy(B_true, W_dagma != 0) # Measure the accuracy of the learned structure using Dagma
print('Accuracy of Dagma:', acc_dagma)

acc_topo = utils.count_accuracy(B_true, W_topo != 0) # Measure the accuracy of the learned structure using Topo
print('Accuracy of Topo:', acc_topo)


W_est = dagrad(X = X, method = 'topo', reg = 'l1', optimizer = 'lbfgs', general_options = {'tuning_method':'decay','K':3})
acc = utils.count_accuracy(B_true, W_est != 0)
print(acc)