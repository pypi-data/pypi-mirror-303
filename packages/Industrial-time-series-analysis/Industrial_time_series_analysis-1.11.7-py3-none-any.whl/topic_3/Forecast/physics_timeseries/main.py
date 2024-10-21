from .wwl_power_data_prepare import power_data_prepare
from .wwl_power_train import Train
from .wwl_power_test import Test
import torch
import os
import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd

# 随机数种子
def seed_it(seed):
    os.environ["PYTHONSEED"] = str(seed)
    np.random.seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True  # 确定性固定
    torch.backends.cudnn.benchmark = True  # False会确定性地选择算法，会降低性能
    torch.backends.cudnn.enabled = True  # 增加运行效率，默认就是True
    torch.manual_seed(seed)

seed_it(1314)

def physics_timeseries(data_path, data_num_per_sample, data_predict_step, train_epoch, model_save_path,
                       device='cpu',
                       loss_save_path='Industrial_time_series_analysis/Forecast/cgran_util/saves/cnn_gru_attention_loss_data.csv',
                       loss_fig_save_path='Industrial_time_series_analysis/Forecast/cgran_util/fig_saves/cnn_gru_attention_loss_fig.png',
                       pre_fig_save_path='Industrial_time_series_analysis/Forecast/cgran_util/fig_saves/cnn_gru_attention_result_fig.png',
                       data_mean_save_path='Industrial_time_series_analysis/Forecast/cgran_util/saves/wwl_oil_data_mean.npy',
                       data_var_save_path='Industrial_time_series_analysis/Forecast/cgran_util/saves/wwl_oil_data_var.npy'
                       ):
    train_set_fea, train_set_tar, val_set_fea, val_set_tar, test_set_fea, test_set_tar = \
        power_data_prepare(data_path, data_mean_save_path, data_var_save_path, data_num_per_sample,
                                               data_predict_step)
    train_loss_his, val_loss_his = Train(train_set_fea, train_set_tar, val_set_fea, val_set_tar,
                                         data_predict_step, model_save_path, train_epoch, device)
    # 保存损失数据为 CSV 文件
    with open(loss_save_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Epoch', 'Training Loss', 'Validation Loss'])
        for epoch, (train, val) in enumerate(zip(train_loss_his, val_loss_his)):
            writer.writerow([epoch, train, val])
    ##  画出损失图
    plt.figure()
    plt.plot(train_loss_his, label='Training Loss')
    plt.plot(val_loss_his, label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.savefig(loss_fig_save_path)
    rmse, mse, r2 = Test(test_set_fea, test_set_tar, model_save_path, data_mean_save_path, data_var_save_path, pre_fig_save_path, device)
    return rmse, mse, r2

# data_path = './dataset/wwl_power_data.csv'    # 数据路径
# data_max_save_path = './saves/wwl_power_data_max.npy'   # 数据归一化存储max路径
# data_min_save_path = './saves/wwl_power_data_min.npy'     # 数据归一化存储min路径
# data_num_per_sample = 36    # 数据分段大小 数据分段大小=历史时间步长+预测时间步长
# data_predict_step = 6   # 预测时间步长
# model_save_path = './saves/phuGru_36_6_model.pkl'    # 模型存储路径
# loss_save_path = './saves/phuGru_loss_data_36_6.csv'     # 训练过程损失值存储路径
# train_epoch = 50       # 训练轮次
# loss_fig_save_path = './fig_saves/phuGru_loss_fig.png'   # loss曲线图存储路径
# result_fig_save_path = './fig_saves/phuGru_result_fig.png'   # 风功率预测值与真实值散点对比图存储路径
#
# # 模型函数所需参数如上所示，包括读取数据路径，训练过程存储的数据路径和一些参数
# rmse, mse, r2 = wwl_power_main(data_path, data_max_save_path, data_min_save_path, data_num_per_sample,
#              data_predict_step, model_save_path, loss_save_path, train_epoch, loss_fig_save_path, result_fig_save_path)
# # 返回模型性能指标rmse, mse和R方
# print(rmse, mse, r2)