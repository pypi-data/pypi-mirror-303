import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns

from tigramite.pcmci import PCMCI
from tigramite.independence_tests.gpdc import GPDC
from tigramite import data_processing as pp, plotting as tp


from industrial_time_series_analysis.Description.Time_Casual.adf_test import adf_test
from industrial_time_series_analysis.Description.Time_Casual.get_optimal_lag_order import lag_order
from industrial_time_series_analysis.Description.Time_Casual.feature_selection import feature_selection

import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

plt.rcParams['font.family'] = 'Times New Roman'  # 设置全局字体为Times New Roman
plt.rcParams.update({'font.size': 16})  # 设置全局字体大小
matplotlib.rcParams['axes.unicode_minus'] = False  # 对于负号的正确显示


def get_causality(data, tau_max, pc_alpha, alpha_level):

    data.index.name = 'time'

    # Convert Pandas DataFrame to the format required by Tigramite
    var_names = data.columns.tolist()
    data_new = data[var_names].values
    dataframe = pp.DataFrame(data_new, var_names=var_names)

    # Initialize the PCMCI and set up the conditional independence test
    pcmci = PCMCI(dataframe=dataframe,
                  cond_ind_test=GPDC(significance='analytic', gp_params=None),
                  verbosity=0)

    # Run the PCMCI algorithm
    results = pcmci.run_pcmci(tau_max=tau_max, pc_alpha=pc_alpha, alpha_level=alpha_level)
    """
        Note: The smaller the pc_alpha, the fewer parents you will get in the PC phase. 
        The smaller the alpha_level, the greater the likelihood of causality in the MCI phase.
    """

    # Extract salient links
    p_matrix = results['p_matrix']
    val_matrix = results['val_matrix']
    sig_links = p_matrix <= alpha_level

    # Sets the edge width to represent the detected significance
    causal_effect = np.where(sig_links, val_matrix, 0)

    # # Draw a cause-and-effect diagram where the thickness of the edges represents the weights
    # tp.plot_graph(
    #     figsize=(6, 4),
    #     val_matrix=causal_effect,
    #     graph=sig_links,
    #     var_names=var_names,
    #     link_colorbar_label='Edge MCI',
    #     node_colorbar_label='Node MCI',
    #     link_width=causal_effect,  # Edge widths are adjusted by weight
    #     node_size=0.2,  # Set the node size
    # )
    # plt.show()
    #
    # for tau_index in range(1, tau_max + 1):
    #     plt.figure(figsize=(8, 6))
    #     sns.heatmap(causal_effect[:, :, tau_index], annot=True, cmap='coolwarm', center=0, vmin=-1, vmax=1,
    #                 fmt=".3f", xticklabels=var_names, yticklabels=var_names)
    #     plt.xlabel(f'Effect variables')
    #     plt.ylabel('Cause variables')
    #     plt.title(f'Causal Effect Matrix at τ={tau_index}')
    #     plt.tight_layout()
    #     plt.show()

    # Store causal results in a DataFrame
    rows = []
    for i in range(causal_effect.shape[0]):
        for j in range(causal_effect.shape[1]):
            for tau_index in range(1, tau_max + 1):
                effect = causal_effect[i, j, tau_index]
                if effect != 0:
                    rows.append([var_names[i], var_names[j], tau_index, effect])

    causality_df = pd.DataFrame(rows, columns=['Cause', 'Effect', 'Lag', 'Causal Effect'])

    return causality_df


if __name__ == '__main__':

    file_path = '../../../data/test_data.xlsx'
    data = pd.read_excel(file_path)

    target_column = 'x13'
    threshold = 0.5
    selected_features, selected_data = feature_selection(data, target_column, threshold)
    print(selected_features, selected_data)

    # Stationary test
    df_diff_stable = adf_test(selected_data)
    print("Stationary-test result：\n", df_diff_stable.head())

    optimal_lag_order = lag_order(df_diff_stable)
    print("optimal_lag_order:", optimal_lag_order)

    pc_alpha = 0.5
    alpha_level = 0.01

    causality_df = get_causality(df_diff_stable, optimal_lag_order, pc_alpha, alpha_level)
    print("causality_df:\n", causality_df)
