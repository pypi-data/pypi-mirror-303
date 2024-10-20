# -*- coding:utf-8 -*-
"""
Name：PanYunJie
Date：2024-07-13
"""
from datetime import datetime
import numpy as np
from torch.utils.data import DataLoader, Subset
from industrial_time_series_analysis.Forecast.forecast_continuous_learning.util.env import set_device
from industrial_time_series_analysis.Forecast.forecast_continuous_learning.util.preprocess import build_loc_net, construct_data
from industrial_time_series_analysis.Forecast.forecast_continuous_learning.util.net_struct import get_feature_map, get_prior_graph_struc
from industrial_time_series_analysis.Forecast.forecast_continuous_learning.datasets.TimeDataset import TimeDataset
from industrial_time_series_analysis.Forecast.forecast_continuous_learning.models import LSTM, MLP, GRU, Transformer, RNN, CNN, GDN, LSTMVAE
import os
import random
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import json
import torch
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

class FCC:

    def train_data_handle(abs_path, train_config, env_config, task_name,adjacency_file_path):
        train_dataset_lst = []
        train_dataloader_lst = []
        val_dataloader_lst = []
        train_model_lst = []
        set_device(env_config['device'])
        adjacency_file_path = adjacency_file_path

        # 训练集封装
        dir_path = f"{abs_path}/data/{env_config['dataset']}/TRain/{task_name}"
        indus_folder = os.listdir(dir_path)
        train_dataset_task = []
        train_dataloader_task = []
        val_dataloader_task = []
        train_model_task = []

        for indus_name in indus_folder:
            indus_file_path = f"{dir_path}/{indus_name}"
            new_dataset_name = f"{env_config['dataset']}/TRain/{task_name}/{indus_name}"
            train_orig = pd.read_csv(os.path.join(indus_file_path, 'train.csv'), sep=',', index_col=0)
            train = train_orig
            if 'attack' in train.columns:  # only test.csv have 'attack' columns
                train = train.drop(columns=['attack'])
            path = indus_file_path
            feature_map = get_feature_map(path)
            graph_struc = get_prior_graph_struc(path,adjacency_file_path)
            fc_edge_index = build_loc_net(graph_struc, list(train.columns), feature_map=feature_map)
            fc_edge_index = torch.tensor(fc_edge_index, dtype=torch.long)
            # 构建训练集
            train_dataset_indata = construct_data(train, feature_map, labels=0)
            cfg = {
                'slide_win': train_config['slide_win'],
                'slide_stride': train_config['slide_stride'],
            }

            train_dataset = TimeDataset(train_dataset_indata, fc_edge_index, mode='train', config=cfg)
            train_dataloader, val_dataloader = FCC.get_loaders(train_dataset,
                                                                train_config['batch'],
                                                                val_ratio=train_config['val_ratio'])

            train_dataloader_task.append(train_dataloader)
            val_dataloader_task.append(val_dataloader)
            train_dataset_task.append(train_dataset)
        train_dataset_task = [item for sublist in train_dataset_task for item in sublist]
        train_dataloader_task = [item for sublist in train_dataloader_task for item in sublist]
        val_dataloader_task = [item for sublist in val_dataloader_task for item in sublist]

        train_dataset_lst.append(train_dataset_task)
        train_dataloader_lst.append(train_dataloader_task)
        val_dataloader_lst.append(val_dataloader_task)
        train_model_lst.append(train_model_task)

        return train_dataloader_task, val_dataloader_task

    def test_data_handle(abs_path, train_config, env_config, task_name,adjacency_file_path):
        test_dataloader_lst = []
        test_dataset_lst = []
        adjacency_file_path = adjacency_file_path

        dir_path = f"{abs_path}/data/{env_config['dataset']}/TEst/{task_name}"
        indus_folder = os.listdir(dir_path)
        test_dataset_task = []
        test_dataloader_task = []
        test_model_task = []

        for indus_name in indus_folder:
            indus_file_path = f"{dir_path}/{indus_name}"
            new_dataset_name = f"{env_config['dataset']}/TEst/{task_name}/{indus_name}"
            test_orig = pd.read_csv(os.path.join(indus_file_path, 'test.csv'), sep=',', index_col=0)
            test = test_orig
            path = indus_file_path
            feature_map = get_feature_map(path)
            graph_struc = get_prior_graph_struc(path,adjacency_file_path)
            fc_edge_index = build_loc_net(graph_struc, list(test.columns), feature_map=feature_map)
            fc_edge_index = torch.tensor(fc_edge_index, dtype=torch.long)
            test_dataset_indata = construct_data(test, feature_map, labels=test.attack.tolist())
            print("----3")
            print(train_config['slide_win'])
            print(train_config['slide_stride'])
            print("----3")
            cfg = {
                'slide_win': train_config['slide_win'],
                'slide_stride': train_config['slide_stride'],
            }
            test_dataset = TimeDataset(test_dataset_indata, fc_edge_index, mode='test', config=cfg)
            test_dataset_task.append(test_dataset)
            test_dataloader_task.append(DataLoader(test_dataset, batch_size=train_config['batch'],
                                                   shuffle=False, num_workers=0, drop_last=True))
            test_dataset_task = [item for sublist in test_dataset_task for item in sublist]
            test_dataloader_task = [item for sublist in test_dataloader_task for item in sublist]
            test_dataset_lst.append(test_dataset_task)
            return test_dataloader_task

    def get_loaders(train_dataset, batch, val_ratio=0.1):
        dataset_len = int(len(train_dataset))
        train_use_len = int(dataset_len * (1 - val_ratio))
        val_use_len = int(dataset_len * val_ratio)
        val_start_index = random.randrange(train_use_len)
        indices = torch.arange(dataset_len)
        train_sub_indices = torch.cat([indices[:val_start_index], indices[val_start_index + val_use_len:]])
        train_subset = Subset(train_dataset, train_sub_indices)
        val_sub_indices = indices[val_start_index:val_start_index + val_use_len]
        val_subset = Subset(train_dataset, val_sub_indices)
        train_dataloader = DataLoader(train_subset, batch_size=batch,
                                      shuffle=True, drop_last=True)
        val_dataloader = DataLoader(val_subset, batch_size=batch,
                                    shuffle=False, drop_last=True)
        return train_dataloader, val_dataloader

    def get_model_pratern(abs_path, task_name, batch_data_name,train_config, env_config,adjacency_file_path):
        train_model_task = []
        dataset = env_config["dataset"]
        path = f"{abs_path}/data/{dataset}/TRain/{task_name}/{batch_data_name}"
        print(path)
        # train_orig = pd.read_csv(os.path.join(path, 'train.csv'), sep=',', index_col=0)
        train_orig = pd.read_csv(f"{abs_path}/data/{dataset}/TRain/{task_name}/{batch_data_name}/train.csv", sep=',', index_col=0)
        train = train_orig
        graph_struc = get_prior_graph_struc(path,adjacency_file_path)
        feature_map = get_feature_map(path)
        fc_edge_index = build_loc_net(graph_struc, list(train.columns), feature_map=feature_map)
        fc_edge_index = torch.tensor(fc_edge_index, dtype=torch.long)
        edge_index_sets = [fc_edge_index]

        if train_config['model'] == "RNN":
            train_model_task.append(RNN.RNNModel(
                dropout_prob=train_config['drop_prob'],
                input_size=len(feature_map),
                hidden_size=train_config['hidden_dim'],
                window_size=train_config['slide_win'],
                num_layers=train_config['num_layers']
            ).to(env_config['num_layers']))

        elif train_config['model'] == "GRU":
            train_model_task.append(GRU.GRUModel(
                dropout_prob=train_config['drop_prob'],
                input_size=len(feature_map),
                hidden_size=train_config['hidden_dim'],
                window_size=train_config['slide_win'],
                num_layers=train_config['num_layers']
            ).to(env_config['num_layers']))


        elif train_config['model'] == "LSTM":
            train_model_task.append(LSTM.LSTModel(
                dropout_prob=train_config['drop_prob'],
                input_size=len(feature_map),
                hidden_size=train_config['hidden_dim'],
                window_size=train_config['slide_win'],
                num_layers=train_config['num_layers']
            ).to(env_config['num_layers']))

        elif train_config['model'] == "LSTMVAE":
            train_model_task.append(LSTMVAE.LSTMVAEModel(
                input_size=len(feature_map),
                hidden_size=train_config['hidden_dim']
            ).to(env_config['num_layers']))


        elif train_config['model'] == "CNN":
            train_model_task.append(CNN.CNNModel(dropout_prob=train_config['drop_prob'],
                                                 input_size=len(feature_map),
                                                 window_size=train_config['slide_win'],
                                                 kernel_length=train_config['kernel_length']
                                                 ).to(env_config['device']))

        elif train_config['model'] == "MLP":
            train_model_task.append(MLP.MLPModel(dropout_prob=train_config['drop_prob'],
                                                 input_size=len(feature_map),
                                                 window_size=train_config['slide_win'],
                                                 fc1_size=train_config['fc1_size'],
                                                 fc2_size=train_config['fc2_size'],
                                                 ).to(env_config['device']))


        elif train_config['model'] == "Transformer":
            train_model_task.append(Transformer.TransformerModel(
                input_size=len(feature_map),
                d_model=train_config['d_model'],
                window_size=train_config['slide_win'],
                num_heads=train_config['num_heads'],
                num_layers=train_config['num_layers'],
                dropout_prob=train_config['drop_prob']
            ).to(env_config['device']))

        elif train_config['model'] == "GDN":
            train_model_task.append(GDN.GDN(edge_index_sets, len(feature_map),
                                            dim=train_config['dim'],
                                            input_dim=train_config['slide_win'],
                                            out_layer_num=train_config['out_layer_num'],
                                            out_layer_inter_dim=train_config['out_layer_inter_dim'],
                                            topk=train_config['topk'],
                                            prior_graph=train_config["graph_struct"]
                                            ).to(env_config['device']))
        return train_model_task

    def peizhi(graph_struct=0, model="CNN", use_ewc=0, batch=32, epoch=200, slide_win=15, slide_stride=1,save_path_pattern="",
               dataset='steel', device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu'), comment="", dim=32, out_layer_num=1, out_layer_inter_dim= 32,topk=4,
               drop_prob=0.1,hidden_dim=64, num_heads=2, num_layers=1, d_model=8, kernel_length=3, fc1_size=512,
               fc2_size=256,decay=0,val_ratio=0.1,sensor_num=7,report='best',load_model_path=""):
        train_config = {
            'graph_struct': graph_struct,
            'model': model,
            'use_ewc': use_ewc,
            'batch': batch,
            'epoch': epoch,
            'slide_win': slide_win,
            'slide_stride': slide_stride,
            'comment': comment,
            'decay': decay,
            'val_ratio': val_ratio,
            'dim': dim,
            'out_layer_num': out_layer_num,
            'out_layer_inter_dim': out_layer_inter_dim,
            'topk': topk,
            'drop_prob': drop_prob,
            'hidden_dim': hidden_dim,
            'num_heads': num_heads,
            'num_layers': num_layers,
            'd_model': d_model,
            'sensor_num': sensor_num,
            'kernel_length': kernel_length,
            'fc1_size': fc1_size,
            'fc2_size': fc2_size
        }

        env_config = {
            'save_path': save_path_pattern,
            'dataset': dataset,
            'report': report,
            'device': device,
            'load_model_path': load_model_path
        }


        return train_config,  env_config


    def get_save_path( train_config, env_config, task_idx):

        dir_path = env_config['save_path']
        dataset = env_config['dataset']
        model = train_config['model']
        datestr = None

        if datestr is None:
            now = datetime.now()
            datestr = now.strftime('%m|%d-%H:%M:%S')

        paths = [
            f'./pretrained/{dir_path}/{dataset}/Task{task_idx}/{model}_task{task_idx}.pt',
            f'./results/{dir_path}/{dataset}/Task{task_idx}/{model}_task{task_idx}.csv',
            f'./results/{dir_path}/{dataset}/Task{task_idx}/{model}_task{task_idx}.png',
        ]
        # paths = [
        #     f'D:/Industrial_time_series_analysis/pretrained/{dataset}/Task{task_idx}/{model}_task{task_idx}.pt',
        #     f'D:/Industrial_time_series_analysis/results/{dataset}/Task{task_idx}/{model}_task{task_idx}.csv',
        #     f'D:/Industrial_time_series_analysis/results/{dataset}/Task{task_idx}/{model}_task{task_idx}.png',
        # ]




        for path in paths:
            dirname = os.path.dirname(path)
            Path(dirname).mkdir(parents=True, exist_ok=True)

        return paths

    def plot_anomalies(train_config, prediction, observation, task_idx):
        plt.figure(figsize=(12, 8), dpi=160)
        font1 = {'family': 'Arial', 'weight': 'normal', 'size': 18}
        ch_num = train_config["sensor_num"]  # 选择要画图的sensor
        time_points = len(prediction)
        t = np.arange(0, time_points)
        prediction = np.asarray(prediction)
        observation = np.asfarray(observation)

        # 反归一化
        if task_idx == 0:
            min_val = 0.02
            max_val = 4.2152
        elif task_idx == 1:
            min_val = 0.06
            max_val = 2.2228
        else:
            min_val = 0.0996
            max_val = 1.9472

        pre = prediction[:, ch_num] * (max_val - min_val) + min_val
        obs = observation[:, ch_num] * (max_val - min_val) + min_val
        plt.plot(t, pre, label='prediction', color='black')
        plt.plot(t, obs, label='observation', color='green')

        plt.legend(prop=font1, loc='upper center', ncol=2)
        plt.xlabel('Time (Second)', fontproperties='Times New Roman', fontsize=20)
        plt.xticks(fontproperties='Arial', fontsize=16)
        plt.ylabel('Value', fontproperties='Times New Roman', fontsize=20)
        plt.yticks(fontproperties='Arial', fontsize=16)
        # img_save_path = self.get_save_path(task_idx)[2]

        dirname = f"results/task{task_idx + 1}"
        Path(dirname).mkdir(parents=True, exist_ok=True)

        plt.savefig(f'{dirname}/compare_label.png')
        plt.show()
        plt.close()
        # 绘制回归散点图
        sns.regplot(x=obs, y=pre, scatter=True)
        plt.title(f'Scatter Plot with Regression Line')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.savefig(f'{dirname}/scatter.png')
        plt.show()
        plt.close()
        # 计算并绘制方差分布图
        residuals = pre - (2 * obs)  # 计算残差
        sns.histplot(residuals, kde=True)
        plt.title('Residuals Distribution')
        plt.xlabel('Residuals')
        plt.ylabel('Frequency')
        plt.savefig(f'{dirname}/resid.png')
        plt.show()
        plt.close()
        # 评价指标
        # 计算均方根误差 (RMSE)
        rmse = np.sqrt(mean_squared_error(obs, pre))
        print("RMSE:", rmse)
        # 计算平均绝对误差 (MAE)
        mae = mean_absolute_error(obs, pre)
        print("MAE:", mae)
        # 计算 R^2 (R-Squared)
        r_squared = r2_score(obs, pre)
        print("R^2:", r_squared)
        # # 计算平均百分比误差 (MAPE)
        # mape = self.mean_absolute_percentage_error(observation, prediction)
        # print("MAPE:", mape)

    def save_list(data, env_config, task):
        dir_path = env_config['save_path']
        dataset = env_config['dataset']
        filename = f'./pretrained/{dir_path}/{dataset}/{task}.json'
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_list(env_config, task):
        dir_path = env_config['save_path']
        dataset = env_config['dataset']
        filename = f'./pretrained/{dir_path}/{dataset}/{task}.json'
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data




