import numpy as np
import matplotlib.pyplot as plt
import torch
from sklearn.metrics import r2_score

def Test(feature_set_test, target_set_test, model_path, data_max_path, data_min_path, fig_save_path, device):
    device = torch.device(device)
    model = torch.load(model_path)

    feature_set_test = feature_set_test.to(device)
    target_set_test = target_set_test.to(device)

    predict = model(feature_set_test, target_set_test)

    # 归一化所做的事情：
    # 先将风速拿出，然后将进行归一化并记录均值和方差，最后将风速加到最后一列
    # 反归一化要做的事情：
    # 将预测出的功率还原，将实际的功率还原
    d_max = torch.tensor(np.load(data_max_path)[0]).to(device)
    d_min = torch.tensor(np.load(data_min_path)[0]).to(device)
    wind_max = torch.tensor(np.load(data_max_path)[1]).to(device)
    wind_min = torch.tensor(np.load(data_min_path)[1]).to(device)
    predict = torch.mul(predict, d_max - d_min) + d_min
    true = torch.mul(target_set_test[:, :, 0], d_max - d_min) + d_min
    wind = torch.mul(target_set_test[:, :, 1], wind_max - wind_min) + wind_min
    # wind = target_set_test[:, :, 12]
    wind = wind.permute(1, 0)

    true = true.permute(1, 0)

    # 计算mse
    mse_fn = torch.nn.MSELoss(reduction='mean')
    mse = mse_fn(predict, true)
    rmse = torch.sqrt(mse)
    print('模型数据')
    print('mse', mse)
    print('rmse', rmse)

    # 计算mae 怎么pytorch没有mae函数？
    m = torch.abs(predict - true)
    print('mae', torch.mean(m))

    # 计算 r2
    predict = predict.detach().to('cpu')
    true = true.detach().to('cpu')

    r2 = r2_score(true, predict)
    print('r2 score', r2)

    wind = wind.detach().to('cpu')
    predict = predict.ravel()
    true = true.ravel()
    wind = wind.ravel()
    plt.figure()
    plt.scatter(wind, predict, label='预测值')
    plt.scatter(wind, true, label='真值')
    # plt.plot(predict, label='预测值')
    # plt.plot(true, label='真值')
    # plt.xlabel('风速（m/s）')
    # plt.ylabel('功率值')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
    # plt.title('风功率散点图')
    plt.legend()
    plt.savefig(fig_save_path)
    plt.show()
    return rmse, mse, r2