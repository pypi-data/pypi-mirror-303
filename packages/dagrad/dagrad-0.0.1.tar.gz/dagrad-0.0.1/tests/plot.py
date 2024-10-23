import seaborn as sns
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
def find_optimal_lambda1_index_decay(err):
    optimal_lambda1_index = 0
    for i in range(len(err)-2,0,-1):
        if err[i] > err[i+1]:
            optimal_lambda1_index = i+1
            break
    return optimal_lambda1_index


def heatplot(dir_name, file_name, reg = 'l1', save = False):
    path = os.getcwd() +  '/tests/experiments/' + dir_name + '/'
    PD = pd.read_csv(path+file_name + '.csv')
    grid_pd = PD[(PD['reg'] == reg) & (PD['selection_method'] == 'grid')]
    cv_pd = PD[(PD['reg'] == reg) & (PD['selection_method'] == 'cv')]
    decay_pd = PD[(PD['reg'] == reg) & (PD['selection_method'] == 'decay')]
    decay_plus_pd = PD[(PD['reg'] == reg) & (PD['selection_method'] == 'decay_plus')]
    method = PD['method'].values[0]
    if reg == 'l1':
        shds = grid_pd['shd'].values
        lambda1s = grid_pd['lambda1'].values
        shds_reshaped = shds.reshape(1, -1)
        optimal_lambda1_cv = cv_pd.loc[cv_pd['err'].idxmin()]['lambda1']
        optimal_lambda1_cv_index = np.where(lambda1s == optimal_lambda1_cv)[0][0]
        optimal_lambda1_decay_index= find_optimal_lambda1_index_decay(decay_pd.sort_values(by='lambda1')['err'].tolist())
        optimal_lambda1_decay_plus_index = find_optimal_lambda1_index_decay(decay_plus_pd.sort_values(by='lambda1')['err'].tolist())
        plt.figure(figsize=(10, 2))
        sns.heatmap(shds_reshaped, annot=True, fmt="d", cmap="viridis", xticklabels=lambda1s, yticklabels=["SHD"])
        plt.text(optimal_lambda1_cv_index + 0.5, 0.8, r'[cv]', color='white', ha='center', va='center')
        plt.text(optimal_lambda1_decay_index + 0.2, 0.2, r'[decay]', color='white', ha='center', va='center')
        plt.text(optimal_lambda1_decay_plus_index + 0.8, 0.2, r'[decay+]', color='white', ha='center', va='center')
        plt.xlabel("lambda")
        plt.title(f"{method}")
        if save:
            from matplotlib.backends.backend_pdf import PdfPages
            from pathlib import Path
            save_path = os.getcwd() + '/tests/plot/' + dir_name + '/'
            Path(save_path).mkdir(parents=True, exist_ok=True)
            pdf_path = f'{save_path}/{file_name}.pdf'
            with PdfPages(pdf_path) as pdf:
                pdf.savefig()
                print(f"Saved to {pdf_path}")
                plt.close()
            #plt.savefig(f'{os.getcwd()}/{file_name}_box.png', dpi=300, bbox_inches='tight')
        # plt.show()


    elif reg =='mcp':
        lambda1s = list(grid_pd['lambda1'].unique())
        lambda1s.sort()
        gammas = list(grid_pd['gamma'].unique())
        gammas.sort()
        pivot_table = grid_pd.pivot(index = "gamma", columns="lambda1", values="shd")

        optimal_lambda1_cv = cv_pd.loc[cv_pd['err'].idxmin()]['lambda1']
        optimal_gamma_cv = cv_pd.loc[cv_pd['err'].idxmin()]['gamma']
        
        optimal_lambda1_cv_index = np.where(lambda1s == optimal_lambda1_cv)[0][0]
        optimal_gamma_cv_index = np.where(gammas == optimal_gamma_cv)[0][0]

        decay_err = list(decay_pd['err'].values)
        decay_err = decay_err[::-1]
        optimal_lambda1_decay_index = find_optimal_lambda1_index_decay(decay_err)
        
        decay_plus_err = list(decay_plus_pd['err'].values)
        decay_plus_err = decay_plus_err[::-1]
        optimal_lambda1_decay_plus_index = find_optimal_lambda1_index_decay(decay_plus_err)
        # Plot the heatmap
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_table, annot=True, fmt="d", cmap="viridis", linewidths=0.5)
        plt.text(optimal_lambda1_cv_index + 0.5, optimal_gamma_cv_index+ 0.8, r'[cv]', color='white', ha='center', va='center')
        plt.text(optimal_lambda1_decay_index + 0.2, optimal_lambda1_decay_index+0.2, r'[decay]', color='white', ha='center', va='center')
        plt.text(optimal_lambda1_decay_plus_index + 0.8, optimal_lambda1_decay_plus_index+0.2, r'[decay+]', color='white', ha='center', va='center')
        plt.title(f"{method}")
        plt.xlabel("lambda1")
        plt.ylabel("gamma")
        if save:
            from matplotlib.backends.backend_pdf import PdfPages
            from pathlib import Path
            save_path = os.getcwd() + '/tests/plot/' + dir_name + '/'
            Path(save_path).mkdir(parents=True, exist_ok=True)
            pdf_path = f'{save_path}/{file_name}.pdf'
            with PdfPages(pdf_path) as pdf:
                pdf.savefig()
                print(f"Saved to {pdf_path}")
                plt.close()
            #plt.savefig(f'{os.getcwd()}/{file_name}_box.png', dpi=300, bbox_inches='tight')
        # plt.show()

if __name__ == '__main__':
    # heatplot('Hyperparameter_tuning_mcp_notears','10_2_ER_linear_gauss', reg = 'mcp', save = True)

    ds = [10, 20, 30, 50, 70]
    ks = [1,2,4]
    graphs = ['ER','SF']
    for d in ds:
        for k in ks:
            for graph in graphs:
                try:
                    heatplot(f'Hyperparameter_tuning_mcp_dagma_uneqvar',f'{d}_{k}_{graph}_linear_gauss', reg = 'l1', save = False)
                except:
                    print(f'Error in {d}_{k}_{graph}_linear_gauss')
                    continue