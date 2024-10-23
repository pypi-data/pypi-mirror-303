import os, subprocess
import numpy as np

no_exp = 5
no_exp_each_run = 5
SEEDS = np.random.randint(10000, size=no_exp)
SEEDS_list = list(SEEDS)
SEEDS_sublists = [SEEDS_list[i:i + no_exp_each_run] for i in range(0, len(SEEDS_list), no_exp_each_run)]
ns = [1000]
NUM_NODES = [10]
DIR_NAME = 'Linear'
graphs = ['ER']
ks = [1]
model = 'linear'
methods_col = ['notears_linear_original', 'notears_linear_numpy','notears_linear_torch']
# methods_col = ['notears_linear_numpy','notears_linear_torch','notears_linear_original',
#             'dagma_linear_numpy','dagma_linear_torch','dagma_linear_original',
#             'topo_linear_numpy','topo_linear_original',
#             'notears_nonlinear_original','notears_nonlinear_torch',
#             'dagma_nonlinear_original','dagma_nonlinear_torch',
#             'topo_nonlinear_original','topo_nonlinear_torch']
# 

job_directory = f"/home/cdeng00/DAGLEARNER/tests/"
job_file = os.path.join(job_directory, "runner.sh")
for n in ns:
    for d in NUM_NODES:
        for k in ks:
            for graph in graphs:
                for methods in methods_col:
                    for it in range(len(SEEDS_sublists)):
                        seeds = SEEDS_sublists[it]

                        job_name = f"{model}_{d}_{k}_{graph}_{methods}_{it}"
                        args1 = f"--seeds {seeds} --n {n} --d {d} --dir_name {DIR_NAME} --graph {graph} --k {k}  --methods {methods}"
                        args2 = f"--model {model}"
                        args1 = args1.replace('[', '').replace(']', '').replace(', ', ' ')
                        args2 = args2.replace('[', '').replace(']', '').replace(', ', ' ')

                        with open(job_file, 'w') as f:
                            f.writelines(f"#!/bin/bash\n")
                            f.writelines(f"#SBATCH --job-name={job_name}\n")
                            f.writelines(f"#SBATCH --output='{job_directory}/out/%A_{job_name}.out'\n")
                            f.writelines(f"#SBATCH --error='{job_directory}/out_error/%A_{job_name}.err'\n")
                            f.writelines(f"#SBATCH --account=phd \n")
                            f.writelines(f"#SBATCH --partition=standard\n")
                            f.writelines("\nunset XDG_RUNTIME_DIR\n")
                            f.writelines("module load conda/23.10")
                            f.writelines("\nsource activate GPT")
                            f.writelines(f"\nsrun --unbuffered python /home/cdeng00/DAGLEARNER/tests/benchmarking_job_runner.py {args1} {args2}")
                        
                        return_code = subprocess.run(f"sbatch {job_file}", shell=True)