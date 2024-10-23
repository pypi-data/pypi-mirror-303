import os, subprocess, sys
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
no_exp = 1
no_exp_each_run = 1
SEEDS = np.random.randint(10000, size=no_exp)
SEEDS_list = list(SEEDS)
SEEDS_sublists = [SEEDS_list[i:i + no_exp_each_run] for i in range(0, len(SEEDS_list), no_exp_each_run)]
ns = [1000]
NUM_NODES = [10,20,30,50,70]
DIR_NAME = 'Hyperparameter_tuning_mcp'
graphs = ['ER','SF']
ks = [1,2,4]
model = 'linear'
selection_methods_collections = [['cv'],['grid'],['decay']['decay_plus']]
method = 'notears'
reg = 'mcp'
K = 5

# NUM_NODES = [10]
# DIR_NAME = 'Hyperparameter_tuning_mcp'
# graphs = ['ER']
# ks = [2]
# model = 'linear'
# selection_methods_collections = [['cv'],['grid'],['decay']]
# method = 'notears'
# reg = 'mcp'
# K = 5

# reg_paras = [0, 0.005, 0.01, 0.05, 0.075, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5]
# lambda1s, gammas 
reg_paras = "[[0,0.05,0.1,0.2,0.3], [1,1.5,2,2.5,3]]"

job_directory = f"/home/cdeng00/DAGlearner/tests/"
job_file = os.path.join(job_directory, "runner.sh")
for n in ns:
    for d in NUM_NODES:
        for k in ks:
            for graph in graphs:
                for selection_methods in selection_methods_collections:
                    for it in range(len(SEEDS_sublists)):
                        seeds = SEEDS_sublists[it]

                        job_name = f"{model}_{d}_{k}_{graph}_{it}"
                        args1 = f"--dir_name {DIR_NAME} --seeds {seeds} --d {d} --n {n}  --graph {graph} --k {k}  --method {method} --selection_methods {selection_methods}"
                        args2 = f"--model {model} --reg {reg} --K {K} --reg_paras {reg_paras}"
                        args1 = args1.replace('[', '').replace(']', '').replace(', ', ' ')
                        # args2 = args2.replace('[', '').replace(']', '').replace(', ', ' ')

                        with open(job_file, 'w') as f:
                            f.writelines(f"#!/bin/bash\n")
                            f.writelines(f"#SBATCH --job-name={job_name}\n")
                            f.writelines(f"#SBATCH --output='{job_directory}/out/%A_{job_name}.out'\n")
                            f.writelines(f"#SBATCH --error='{job_directory}/out_error/%A_{job_name}.err'\n")
                            f.writelines(f"#SBATCH --account=phd \n")
                            f.writelines(f"#SBATCH --partition=standard\n")
                            f.writelines(f"#SBATCH --time=1-23:00:00\n")
                            f.writelines("\nunset XDG_RUNTIME_DIR\n")
                            f.writelines("module load conda/23.10")
                            f.writelines("\nsource activate GPT")
                            f.writelines(f"\nsrun --unbuffered python /home/cdeng00/DAGlearner/tests/hyperparameter_tuning_job.py {args1} {args2}")
                        
                        return_code = subprocess.run(f"sbatch {job_file}", shell=True)