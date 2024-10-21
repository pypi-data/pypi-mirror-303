# Designer:Yunjie Pan
# Time:2024/1/26 23:43
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# downsample by 10
def downsample(data, labels, down_len=1):
    np_data = np.array(data)
    np_labels = np.array(labels)

    orig_len, col_num = np_data.shape

    down_time_len = orig_len // down_len

    np_data = np_data.transpose()  # (629, 8) => (8, 627)

    d_data = np_data[:, :down_time_len * down_len].reshape(col_num, -1, down_len)  # (8, 627) => (8, 627, 1)
    d_data = np.median(d_data, axis=2).reshape(col_num, -1)   # find the median to represent the group (8, 627)
    d_data = d_data.transpose()   # (8, 627) => (627, 8)

    d_labels = np_labels[:down_time_len * down_len].reshape(-1, down_len)
    # if exist anomalies, then this sample is abnormal
    d_labels = np.round(np.max(d_labels, axis=1))

    return d_data.tolist(), d_labels.tolist()

def main():
    raw_data = pd.read_excel('../data/steel/TRain/Task2(拉速1)/板柸2_2数据/板坯2_2.xlsx')
    raw_label = raw_data['label']

    count_anomalies = 0
    for i in range(len(raw_label)):
        if raw_label[i] == 1:
            count_anomalies += 1
    print(f"anomalies:{count_anomalies}, {(count_anomalies / len(raw_label)) * 100:.2f}%")

    print("raw_data.shape:", raw_data.shape)

    # filter columns in excel files
    filter_columns = ["castspeed_2", "h10_ws_fix_ht_ext_2", "h10_ws_left_ht_ext_2", "h10_ws_los_ht_ext_2",
                      "h10_ws_right_ht_ext_2", "actual_gate_position_2", "castspeeddiff_2", "mdleveldiff_2"]
    raw_data = raw_data[filter_columns]

    print("raw_data:", raw_data.head(10))
    print("raw_label.shape:", raw_label.shape)

    rows, columns = raw_data.shape
    raw_data.insert(loc=0, column='timestep', value=np.arange(0, rows, 1))
    print("raw_data.columns:", raw_data.columns)

    raw_data = raw_data.iloc[:, 1:]
    raw_data = raw_data.fillna(raw_data.mean())
    raw_data = raw_data.fillna(0)

    raw_data = raw_data.rename(columns=lambda x: x.strip())
    x_raw_data = raw_data.values




    for i, col in enumerate(raw_data.columns):
        raw_data.loc[:, col] = x_raw_data[:, i]

    # Splitting the raw data into training set and testing set
    print("raw_data.shape:", raw_data.shape)
    split_ratio = 1  # 训练集、测试集划分比例
    train_data = raw_data.iloc[range(0, int(rows * split_ratio))]
    test_data = raw_data.iloc[range(int(rows * split_ratio), rows)]
    train_labels = raw_label[range(0, int(rows * split_ratio))]
    test_labels = raw_label[range(int(rows * split_ratio), rows)]

    d_train_x, d_train_labels = downsample(train_data.values, train_labels, down_len=1)
    d_test_x, d_test_labels = downsample(test_data.values, test_labels, down_len=1)

    train_df = pd.DataFrame(d_train_x, columns=train_data.columns)
    test_df = pd.DataFrame(d_test_x, columns=test_data.columns)

    train_df['attack'] = d_train_labels
    test_df['attack'] = d_test_labels

    # print(train_df.values.shape)
    # print(test_df.values.shape)

    train_df.to_csv('../data/steel/TRain/Task2(拉速1)/板柸2_2数据/train.csv')
    # test_df.to_csv('../data/steel/TEst/Task2(拉速1)/板柸2_4后半段数据/test.csv')
    #
    # f = open('../data/steel/TEst/Task2(拉速1)/板柸2_4后半段数据/list.txt', 'w')
    # for col in raw_data.columns:
    #     f.write(col + '\n')
    # f.close()

    f = open('../../data/steel/TRain/Task2(拉速1)/板柸2_2数据/list.txt', 'w')
    for col in raw_data.columns:
        f.write(col + '\n')
    f.close()


if __name__ == '__main__':
    main()
