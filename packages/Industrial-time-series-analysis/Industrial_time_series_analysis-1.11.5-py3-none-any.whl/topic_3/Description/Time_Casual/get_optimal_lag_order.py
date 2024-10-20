import pandas as pd
from statsmodels.tsa.api import VAR

from industrial_time_series_analysis.Description.Time_Casual.adf_test import adf_test
from industrial_time_series_analysis.Description.Time_Casual.feature_selection import feature_selection


def lag_order(data):

    data.set_index(['time'], inplace=True)
    # 确保索引为 datetime 类型，并指定频率
    data.index = pd.to_datetime(data.index)
    data = data.asfreq('H')  # 假设您的数据频率为2小时，根据实际情况调整

    # 使用VAR模型和AIC准则确定最佳滞后阶数
    model = VAR(data)
    aic_values = []
    bic_values = []
    fpe_values = []
    hqic_values = []
    lags = range(1, 10)  # 可以根据需要调整最大滞后阶数的范围

    for lag in lags:
        result = model.fit(lag)
        aic_values.append(result.aic)
        bic_values.append(result.bic)
        fpe_values.append(result.fpe)
        hqic_values.append(result.hqic)

    # 找到AIC、BIC和HQIC最小的滞后阶数
    min_aic = min(aic_values)
    optimal_lag_aic = lags[aic_values.index(min_aic)]

    min_bic = min(bic_values)
    optimal_lag_bic = lags[bic_values.index(min_bic)]

    min_fpe = min(fpe_values)
    optimal_lag_fpe = lags[fpe_values.index(min_fpe)]

    min_hqic = min(hqic_values)
    optimal_lag_hqic = lags[hqic_values.index(min_hqic)]

    optimal_lag_list = [optimal_lag_aic, optimal_lag_bic, optimal_lag_fpe, optimal_lag_hqic]
    optimal_lag_list_new = list(set([x for x in optimal_lag_list if optimal_lag_list.count(x) > 1]))

    if not optimal_lag_list_new:
        optimal_lag_order = min(optimal_lag_list)
    elif len(optimal_lag_list_new) == 1:
        optimal_lag_order = optimal_lag_list_new[0]
    else:
        optimal_lag_order = min(optimal_lag_list_new)

    return optimal_lag_order


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

