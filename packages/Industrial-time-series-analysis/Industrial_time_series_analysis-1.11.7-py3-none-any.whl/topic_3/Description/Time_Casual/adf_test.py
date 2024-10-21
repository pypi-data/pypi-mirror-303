import pandas as pd
from statsmodels.tsa.stattools import adfuller
from sklearn.preprocessing import MinMaxScaler

from industrial_time_series_analysis.Description.Time_Casual.feature_selection import feature_selection

def assess_stationary_and_diff_order(df, max_diff=5, significance_level=0.05):

    """
        Perform a stationarity test for each variable in the DataFrame, and if it is non-stationary,
        try to perform the difference until stationary, and give the difference order after stationarity.
    """

    stationary_results = {}

    for column in df.columns:
        time_series = df[column]
        diff_order = 0
        p_value = 1

        while diff_order <= max_diff and p_value > significance_level:
            if diff_order > 0:
                time_series = time_series.diff().dropna()
            adf_result = adfuller(time_series)
            p_value = adf_result[1]
            if p_value <= significance_level:
                stationary_results[column] = {'is_stationary': True, 'diff_order': diff_order}
                break
            diff_order += 1

        if p_value > significance_level:
            stationary_results[column] = {'is_stationary': False, 'diff_order': diff_order - 1}

    return stationary_results


def adf_test(selected_df):

    selected_df.set_index(['time'], inplace=True)
    # Normalization
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(selected_df)
    selected_df_scaled = pd.DataFrame(scaled_features, columns=selected_df.columns)

    stationary_results = assess_stationary_and_diff_order(selected_df_scaled)

    # Differential processing for smooth data
    df_diff_stable = pd.DataFrame(index=selected_df.index)
    for column, result in stationary_results.items():
        if result['is_stationary']:
            if result['diff_order'] == 0:
                df_diff_stable[column] = selected_df[column]
            else:
                df_diff_stable[column] = selected_df[column].diff(result['diff_order']).dropna()
        else:
            print(f"Variable '{column}' is still non-stationary after {result['diff_order']} order differencing.")

    # Remove any NaN values due to differential
    df_diff_stable.dropna(inplace=True)

    for variable, result in stationary_results.items():
        print(
            f"Variable '{variable}': Is Stationary? {result['is_stationary']}, Differencing Order Needed: {result['diff_order']}")
    df_diff_stable.reset_index(inplace=True)

    return df_diff_stable


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
