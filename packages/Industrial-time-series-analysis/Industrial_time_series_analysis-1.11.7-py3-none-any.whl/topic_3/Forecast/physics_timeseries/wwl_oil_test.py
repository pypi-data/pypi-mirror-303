import math

import numpy as np
import matplotlib.pyplot as plt
import torch
from sklearn.metrics import r2_score
import pandas as pd

def Test(feature_set_test, target_set_test, model_path, data_mean_path, data_var_path, fig_save_path):
    device = torch.device('cuda')
    model = torch.load(model_path)

    feature_set_test = feature_set_test.to(device)
    target_set_test = target_set_test.to(device)
    predict = model(feature_set_test)
    # 归一化所做的事情：
    # 先将风速拿出，然后将进行归一化并记录均值和方差，最后将风速加到最后一列
    # 反归一化要做的事情：
    # 将预测出的功率还原，将实际的功率还原
    d_mean = torch.tensor(np.load(data_mean_path)[0]).to(device)
    d_var = torch.tensor(np.load(data_var_path)[0]).to(device)
    print(predict.shape)
    predict = torch.mul(predict, d_var+1e-8) + d_mean
    true = torch.mul(target_set_test[:, :, 0], d_var+1e-8) + d_mean

    # 计算mse
    mse_fn = torch.nn.MSELoss(reduction='mean')
    mse = mse_fn(predict, true)
    rmse = torch.sqrt(mse)
    print('模型数据')
    print('mse', mse)
    print('rmse', rmse)

    # 计算mae 怎么pytorch没有mae函数？
    m = torch.abs(predict-true)
    print('mae', torch.mean(m))

    # 计算 r2
    predict = predict.detach().to('cpu')
    true = true.detach().to('cpu')

    r2 = r2_score(true, predict)
    print('r2 score', r2)

    predict = predict.ravel()
    true = true.ravel()
    plt.figure(figsize=(9, 6))
    plt.plot(predict[0:1000], label='预测值')
    plt.plot(true[0:1000], label='真值')
    plt.xlabel('时间点')
    plt.ylabel('温度（℃）')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
    plt.title('齿轮箱轴承温度预测值-真实值对比图')
    plt.legend()
    plt.savefig(fig_save_path)

    return rmse, mse, r2

    # predict = np.array(predict)
    # predict = predict.flatten()
    # true = np.array(true)
    # true = true.flatten()
    # rid = true - predict
    # print(predict.shape)
    # date_range = pd.date_range('2023-01-01', periods=args.predict_step*1000)
    # print(date_range.shape)
    # # 将数据转换为Pandas的Series
    # predicted_ts = pd.Series(predict, index=date_range, name='Predicted')
    # actual_ts = pd.Series(true, index=date_range, name='Actual')
    # # 计算误差（这里使用均方根误差RMSE）
    # rmse = np.sqrt((predicted_ts - actual_ts) ** 2)
    # # 计算EWMA和标准差
    # ewma = rmse.ewm(span=10).mean()  # 使用span参数设置指数加权移动平均的窗口大小
    # # 设置阈值
    # threshold = ewma.mean() + 4 * ewma.std()  # 通常情况下，可以根据需要调整标准差的倍数
    # # plt.plot(predict[0:2000], label='predictData')
    # # plt.plot(true[0:2000], label='trueData')
    # plt.plot(abs(predict-true)[0:1000], label='rid')
    # plt.xlabel('min')
    # plt.ylabel('摄氏度')
    # plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
    # plt.title('Training and Validation Loss')
    # plt.legend()
    # plt.show()

