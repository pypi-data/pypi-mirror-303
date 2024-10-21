import pandas as pd
from sklearn.feature_selection import mutual_info_regression


def feature_selection(data, target_column, threshold):

    # Check if the 'time' column is included
    if 'time' not in data.columns:
        raise ValueError("There is no 'time' column in the DataFrame")

    X = data.drop(columns=['time', target_column])
    y = data[target_column]

    # Computing Mutual Information (Regression Tasks)
    mi = mutual_info_regression(X, y)

    # Create a DataFrame that contains the feature name and mutual information values
    mi_df = pd.DataFrame({'Feature': X.columns, 'Mutual Information': mi})

    # Sort according to mutual information values in descending order
    mi_df = mi_df.sort_values(by='Mutual Information', ascending=False).reset_index(drop=True)

    # Select features with high mutual information values
    selected_features = mi_df[mi_df['Mutual Information'] > threshold]['Feature']
    selected_data = data[['time'] + selected_features.tolist() + [target_column]]

    return selected_features, selected_data


if __name__ == '__main__':

    file_path = '../../../data/test_data.xlsx'
    data = pd.read_excel(file_path)

    target_column = 'x13'
    threshold = 0.5
    selected_features, selected_data = feature_selection(data, target_column, threshold)
    print(selected_features, selected_data)
