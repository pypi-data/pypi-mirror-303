
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def summarize_data(dir_name, variance_name_list = None):
    pd_name = dir_name + '_summary'
    path = os.getcwd() +  '/experiments/' + dir_name + '/'
    if os.path.isfile(os.getcwd()+'/'+pd_name+'.csv'):
        print('Data already summarized, we remove the old data')
        os.remove(os.getcwd()+'/'+pd_name+'.csv')
    for file in os.listdir(path):
        if file.endswith(".csv"):
            df = pd.read_csv(path+file)
            summary_data = {}
            for column in df.columns:
                if df[column].dtype in [np.float64, np.int64]:
                    summary_data[column] = round(df[column].mean(),3)
                    if variance_name_list and column in variance_name_list:
                        if len(df[column]) > 1:
                            summary_data[column+'_std'] = round(df[column].std()/np.sqrt(len(df[column])),3)
                        else:
                            summary_data[column+'_std'] = 0
                elif all(x == df[column][0] for x in df[column]):
                    summary_data[column] = df[column][0]
            pd_summary = pd.DataFrame([summary_data])
            if os.path.isfile(os.getcwd()+'/'+pd_name + '.csv'):
                pd_summary.to_csv(os.getcwd()+'/'+pd_name + '.csv', mode='a', index=False, header=False)
            else:
                pd_summary.to_csv(os.getcwd()+'/'+pd_name + '.csv', index=False, header=True)
            
    pd_summary = pd.read_csv(os.getcwd()+'/'+pd_name + '.csv')
    sorted_pd_summary = pd_summary.sort_values(by=['d','graph','k','method'], ascending=[True,True, True,True])
    sorted_pd_summary.to_csv(os.getcwd()+'/'+pd_name + '.csv', index=False, header=True)

if __name__ == '__main__':
    summarize_data('NonLinear_dagma_Oct17',['shd','runtime'])

        
