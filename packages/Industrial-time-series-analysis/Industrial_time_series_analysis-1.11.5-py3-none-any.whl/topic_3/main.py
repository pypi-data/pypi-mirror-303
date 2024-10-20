# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import torch
from torch.utils.data import DataLoader, Subset
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')

from steel_ewc_test.util.env import get_device, set_device
from steel_ewc_test.util.preprocess import build_loc_net, construct_data
from steel_ewc_test.util.net_struct import get_feature_map, get_fc_graph_struc, get_prior_graph_struc
from steel_ewc_test.util.ewc_utils import EWC
from steel_ewc_test.test import *

from steel_ewc_test.datasets.TimeDataset import TimeDataset

from steel_ewc_test.models import Transformer, LSTMVAE, GRU, CNN, GDN, RNN, LSTM, MLP

from steel_ewc_test.train import train_on_batch
from datetime import datetime
import os
import argparse
from pathlib import Path

import random


# # 在每个任务结束后对数据集、数据加载器和模型列表进行相同的随机重排
# def shuffle_lists(lst1, lst2, lst3, lst4):
#     combined = list(zip(lst1, lst2, lst3, lst4))
#     random.shuffle(combined)
#     return zip(*combined)

# 在第二个任务结束后，仅对新添加的部分进行单独的随机重排
# def shuffle_additional_lists(prev_lst1, prev_lst2, prev_lst3, prev_lst4, new_lst1, new_lst2, new_lst3, new_lst4):
#     # 合并
#     combined = list(zip(prev_lst1 + new_lst1, prev_lst2 + new_lst2, prev_lst3 + new_lst3, prev_lst4 + new_lst4))
#     # 对新添加的部分进行单独的随机重排
#     new_combined = combined[len(prev_lst1):]
#     random.shuffle(new_combined)
#     # 将重新排序的新部分与未排序的旧部分合并
#     combined = combined[:len(prev_lst1)] + new_combined
#     prev_lst1, prev_lst2, prev_lst3, prev_lst4 = zip(*combined)
#     return list(prev_lst1), list(prev_lst2), list(prev_lst3), list(prev_lst4)
#     #return zip(*combined)

class Main():
    def __init__(self, train_config, env_config, debug=False):

        self.train_config = train_config
        self.env_config = env_config
        self.datestr = None

        self.dataset = self.env_config['dataset']
        self.model_name = self.train_config['model']

        # 分别给训练集和测试集创建路径
        print("os.cwd():", os.getcwd())
        self.task_TRain_names = os.listdir(f"../data/{self.dataset}/TRain")
        self.task_TEst_names = os.listdir(f"../data/{self.dataset}/TEst")
        print("task_TRain_names:", self.task_TRain_names)
        print("task_TEst_names:", self.task_TEst_names)

        # 训练集测试集列表
        self.train_dataset_lst = []
        self.test_dataset_lst = []
        self.train_dataloader_lst = []
        self.val_dataloader_lst = []
        self.test_dataloader_lst = []
        self.train_model_lst = []
        self.train_model_name_lst = []
        self.test_model_lst = []
        self.test_model_name_lst = []

        set_device(env_config['device'])
        self.device = get_device()

        # 训练集封装
        for task_name in self.task_TRain_names:
            dir_path = f"../data/{self.dataset}/TRain/{task_name}"
            steel_folder = os.listdir(dir_path)
            print("steel_folder:", steel_folder)
            train_dataset_task = []
            train_dataloader_task = []
            val_dataloader_task = []
            train_model_task = []

            for steel_name in steel_folder:
                steel_file_path = f"{dir_path}/{steel_name}"
                new_dataset_name = f"{self.dataset}/TRain/{task_name}/{steel_name}"
                print("new_dataset_name:", new_dataset_name)
                train_orig = pd.read_csv(os.path.join(steel_file_path, 'train.csv'), sep=',', index_col=0)

                train = train_orig

                if 'attack' in train.columns:  # only test.csv have 'attack' columns
                    train = train.drop(columns=['attack'])

                # 通过list.txt获取所有sensor信息
                feature_map = get_feature_map(new_dataset_name)

                # 构建图网络结构
                if self.train_config["graph_struct"] == 0:
                    graph_struc = get_prior_graph_struc(new_dataset_name)
                else:
                    graph_struc = get_fc_graph_struc(new_dataset_name)

                # 利用图构建各Sensor之间的依赖关系
                fc_edge_index = build_loc_net(graph_struc, list(train.columns), feature_map=feature_map)
                fc_edge_index = torch.tensor(fc_edge_index, dtype=torch.long)

                # 构建训练集
                train_dataset_indata = construct_data(train, feature_map, labels=0)
                cfg = {
                    'slide_win': train_config['slide_win'],
                    'slide_stride': train_config['slide_stride'],
                }

                train_dataset = TimeDataset(train_dataset_indata, fc_edge_index, mode='train', config=cfg)
                train_dataloader, val_dataloader = self.get_loaders(train_dataset,
                                                                    train_config['batch'],
                                                                    val_ratio=train_config['val_ratio'])

                train_dataloader_task.append(train_dataloader)
                val_dataloader_task.append(val_dataloader)
                train_dataset_task.append(train_dataset)

            train_dataset_task = [item for sublist in train_dataset_task for item in sublist]
            train_dataloader_task = [item for sublist in train_dataloader_task for item in sublist]
            val_dataloader_task = [item for sublist in val_dataloader_task for item in sublist]
            edge_index_sets = [fc_edge_index]

            if self.model_name == "RNN":
                train_model_task.append(RNN.RNNModel(
                    dropout_prob=train_config['drop_prob'],
                    input_size=len(feature_map),
                    hidden_size=train_config['hidden_dim'],
                    window_size=train_config['slide_win'],
                    num_layers=train_config['num_layers']
                ).to(self.device))

            elif self.model_name == "GRU":
                train_model_task.append(GRU.GRUModel(
                    dropout_prob=train_config['drop_prob'],
                    input_size=len(feature_map),
                    hidden_size=train_config['hidden_dim'],
                    window_size=train_config['slide_win'],
                    num_layers=train_config['num_layers']
                ).to(self.device))


            elif self.model_name == "LSTM":
                train_model_task.append(LSTM.LSTModel(
                    dropout_prob=train_config['drop_prob'],
                    input_size=len(feature_map),
                    hidden_size=train_config['hidden_dim'],
                    window_size=train_config['slide_win'],
                    num_layers=train_config['num_layers']
                ).to(self.device))

            elif self.model_name == "LSTMVAE":
                train_model_task.append(LSTMVAE.LSTMVAEModel(
                    input_size=len(feature_map),
                    hidden_size=train_config['hidden_dim']
                ).to(self.device))


            elif self.model_name == "CNN":
                train_model_task.append(CNN.CNNModel(dropout_prob=train_config['drop_prob'],
                                                     input_size=len(feature_map),
                                                     window_size=train_config['slide_win'],
                                                     kernel_length=train_config['kernel_length']
                                                     ).to(self.device))

            elif self.model_name == "MLP":
                train_model_task.append(MLP.MLPModel(dropout_prob=train_config['drop_prob'],
                                                     input_size=len(feature_map),
                                                     window_size=train_config['slide_win'],
                                                     fc1_size=train_config['fc1_size'],
                                                     fc2_size=train_config['fc2_size'],
                                                     ).to(self.device))


            elif self.model_name == "Transformer":
                train_model_task.append(Transformer.TransformerModel(
                    input_size=len(feature_map),
                    d_model=train_config['d_model'],
                    window_size=train_config['slide_win'],
                    num_heads=train_config['num_heads'],
                    num_layers=train_config['num_layers'],
                    dropout_prob=train_config['drop_prob']
                ).to(self.device))

            elif self.model_name == "GDN":
                train_model_task.append(GDN.GDN(edge_index_sets, len(feature_map),
                                                dim=train_config['dim'],
                                                input_dim=train_config['slide_win'],
                                                out_layer_num=train_config['out_layer_num'],
                                                out_layer_inter_dim=train_config['out_layer_inter_dim'],
                                                topk=train_config['topk'],
                                                prior_graph=self.train_config["graph_struct"]
                                                ).to(self.device))

            self.train_dataset_lst.append(train_dataset_task)
            self.train_dataloader_lst.append(train_dataloader_task)
            self.val_dataloader_lst.append(val_dataloader_task)
            self.train_model_lst.append(train_model_task)

        # 测试集封装
        for task_name in self.task_TEst_names:
            dir_path = f"../data/{self.dataset}/TEst/{task_name}"
            steel_folder = os.listdir(dir_path)
            print("steel_folder:", steel_folder)
            test_dataset_task = []
            test_dataloader_task = []
            test_model_task = []

            for steel_name in steel_folder:
                steel_file_path = f"{dir_path}/{steel_name}"
                new_dataset_name = f"{self.dataset}/TEst/{task_name}/{steel_name}"
                print("new_dataset_name:", new_dataset_name)
                test_orig = pd.read_csv(os.path.join(steel_file_path, 'test.csv'), sep=',', index_col=0)

                test = test_orig

                # 通过list.txt获取所有sensor信息
                feature_map = get_feature_map(new_dataset_name)

                # 构建图网络结构
                if self.train_config["graph_struct"] == 0:
                    graph_struc = get_prior_graph_struc(new_dataset_name)
                else:
                    graph_struc = get_fc_graph_struc(new_dataset_name)

                # 利用图构建各Sensor之间的依赖关系
                fc_edge_index = build_loc_net(graph_struc, list(test.columns), feature_map=feature_map)
                fc_edge_index = torch.tensor(fc_edge_index, dtype=torch.long)

                # 构建测试集
                test_dataset_indata = construct_data(test, feature_map, labels=test.attack.tolist())

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
            self.test_dataset_lst.append(test_dataset_task)
            self.test_dataloader_lst.append(test_dataloader_task)

    def run(self):
        num_tasks = len(self.task_TRain_names)
        print('num_tasks:', num_tasks)
        self.ewc = None
        self.pre_model = None

        # 多任务持续学习（训练）
        for task_idx in range(num_tasks):
            if task_idx == 0:
                dir_path = f"data/{self.dataset}/TRain/Task1(拉速1.2)"
            elif task_idx == 1:
                dir_path = f"data/{self.dataset}/TRain/Task2(拉速1)"
            else:
                dir_path = f"data/{self.dataset}/TRain/Task3(拉速1.4)"
            print('dir_path:', dir_path)

            # # 第一个任务无需使用EWC，任务二、任务三才使用EWC
            # old_tasks = []
            # if task_idx  >= 1 and self.train_config['use_ewc'] == 1:
            #     print('使用弹性权重巩固值')
            #     # old_tasks = self.train_dataset_lst[task_idx-1]
            #     # 在先前的任务索引范围内进行迭代，包括当前任务。
            #     for sub_task in range(0,task_idx):
            #         old_tasks.append(self.train_dataset_lst[sub_task])
            #         print('sub_task:',sub_task)
            #         # 遍历当前先前子任务的数据集列表  将当前先前子任务的数据集添加到 old_tasks 列表中。
            #         # for sub_dataset in self.train_dataset_lst[sub_task]:
            #         #     old_tasks.append(sub_dataset)

            # 为每个任务下模型设置设置保存路径（训练）
            # for steel_idx, steel_name in enumerate(steel_names):
            #     print("enenen",enumerate(steel_names))
            if len(self.env_config['load_model_path']) > 0:
                model_save_path = self.env_config['load_model_path']
            else:
                model_save_path = self.get_save_path(task_idx)[0]


            self.cur_model = self.train_model_lst[task_idx][0]
            self.pre_modeldar = self.train_model_lst[task_idx][0]
            self.pre_model = self.train_model_lst[task_idx][0]

            if task_idx >= 1:
                # 加载前一个任务模型参数用于弹性权重巩固
                pre_task_idx = task_idx - 1
                load_model_path = f'./pretrained/{self.dataset}/Task{task_idx}/{self.model_name}_task{pre_task_idx + 1}.pt'
                # 加载load_model_path前一个任务的模型状态字典到self.pre_model。
                self.pre_model.load_state_dict(torch.load(load_model_path))

            # print('未进去前', len(self.train_dataset_lst[0]))
            if task_idx >= 1 and self.train_config['use_ewc'] == 1:
                self.ewc = EWC(self.pre_model, task_idx, old_datasetss=self.train_dataloader_lst,
                               model_name=self.model_name)

            # print(f"start training {task_idx + 1}.............")
            train_on_batch(self.cur_model, model_save_path, self.pre_model,
                           config=self.train_config,
                           train_dataloader=self.train_dataloader_lst[task_idx],
                           val_dataloader=self.val_dataloader_lst[task_idx],
                           ewc=self.ewc
                           )

            # test
            self.cur_model.load_state_dict(torch.load(model_save_path))

            best_model = self.cur_model.to(self.device)

            _, test_result = test(best_model, self.test_dataloader_lst[task_idx],
                                  model_name=self.model_name)

            # pred_labels = self.get_score(test_result)

            prediction, observation, gt_labels = test_result
            # pdb.set_trace()

            self.plot_anomalies(prediction, observation, task_idx, 0)

    def get_loaders(self, train_dataset, batch, val_ratio=0.1):
        dataset_len = int(len(train_dataset))
        train_use_len = int(dataset_len * (1 - val_ratio))
        print(dataset_len)
        val_use_len = int(dataset_len * val_ratio)
        val_start_index = random.randrange(train_use_len)

        print(val_start_index)
        # val_start_index = 120

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

    def get_save_path(self, task_idx):

        dir_path = self.env_config['save_path']

        if self.datestr is None:
            now = datetime.now()
            self.datestr = now.strftime('%m|%d-%H:%M:%S')

        paths = [
            f'./pretrained/{dir_path}/{self.dataset}/Task{task_idx + 1}/{self.model_name}_task{task_idx + 1}.pt',
            f'./results/{dir_path}/{self.dataset}/Task{task_idx + 1}/{self.model_name}_task{task_idx + 1}.csv',
            f'./results/{dir_path}/{self.dataset}/Task{task_idx + 1}/{self.model_name}_task{task_idx + 1}.png',
        ]

        for path in paths:
            dirname = os.path.dirname(path)
            Path(dirname).mkdir(parents=True, exist_ok=True)

        return paths

    def plot_anomalies(self, prediction, observation, task_idx, steel_idx):
        plt.figure(figsize=(12, 8), dpi=160)
        font1 = {'family': 'Arial', 'weight': 'normal', 'size': 18}
        ch_num = self.train_config["sensor_num"]  # 选择要画图的sensor
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

        # pre = prediction[:, ch_num]
        # obs = observation[:, ch_num]
        # pre = prediction[:, ch_num]
        # obs = observation[:, ch_num]
        # print(obs)

        plt.plot(t, pre, label='prediction', color='black')
        plt.plot(t, obs, label='observation', color='green')
        # print(obs)

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


def model_exp(model_name=None, dataset=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-graph_struct', help='0-Prior Graph, 1-Learn Graph', type=int, default='0')
    parser.add_argument('-model', help='RNN/ GRU/ LSTM/ LSTMVAE/ CNN/ MLP/ Transformer/ GDN', type=str,
                        default="CNN")
    parser.add_argument('-use_ewc', help='0-w/o ewc, 1-w/ ewc', type=int, default="1")
    parser.add_argument('-batch', help='batch size', type=int, default=32)
    parser.add_argument('-epoch', help='train epoch', type=int, default=200)
    parser.add_argument('-slide_win', help='slide_win', type=int, default=15)
    parser.add_argument('-slide_stride', help='slide_stride', type=int, default=1)
    parser.add_argument('-save_path_pattern', help='save path pattern', type=str, default='')
    parser.add_argument('-dataset', help='steel or other datasets', type=str, default='steel')
    parser.add_argument('-device', help='cuda / cpu', type=str, default='cuda')
    # parser.add_argument('-random_seed', help='random seed', type=int, default=0)
    parser.add_argument('-comment', help='experiment comment', type=str, default='')

    # For GDN
    parser.add_argument('-dim', help='dimension', type=int, default=32)
    parser.add_argument('-out_layer_num', help='outlayer num', type=int, default=1)
    parser.add_argument('-out_layer_inter_dim', help='out_layer_inter_dim', type=int, default=32)
    parser.add_argument('-topk', help='topk num', type=int, default=4)

    # For RNN/ GRU/ LSTM/ LSTMVAE/ Transformer
    parser.add_argument('-drop_prob', help='dropout probability', type=float, default=0.1)
    parser.add_argument('-hidden_dim', help='hidden dimension', type=int, default=64)
    parser.add_argument('-num_heads', help='number of multi-heads', type=int, default=2)
    parser.add_argument('-num_layers', help='number of layers', type=int, default=1)
    parser.add_argument('-d_model', help='model dimension', type=int, default=8)

    # For CNN
    parser.add_argument('-kernel_length', help='kernel length', type=int, default=3)

    # For MLP
    parser.add_argument('-fc1_size', help='fcUnit2 Size', type=int, default=512)
    parser.add_argument('-fc2_size', help='fcUnit2 Size', type=int, default=256)

    parser.add_argument('-decay', help='decay', type=float, default=0)
    parser.add_argument('-val_ratio', help='val ratio', type=float, default=0.1)

    parser.add_argument('-sensor_num', help='sensor for plotting', type=str, default=7)
    parser.add_argument('-report', help='best / val', type=str, default='best')
    parser.add_argument('-load_model_path', help='trained model path', type=str, default='')

    args = parser.parse_args()

    # random.seed(args.random_seed)
    # np.random.seed(args.random_seed)
    # torch.manual_seed(args.random_seed)
    # torch.cuda.manual_seed(args.random_seed)
    # torch.cuda.manual_seed_all(args.random_seed)
    # torch.backends.cudnn.benchmark = False
    # torch.backends.cudnn.deterministic = True
    # os.environ['PYTHONHASHSEED'] = str(args.random_seed)

    train_config = {
        'graph_struct': args.graph_struct,
        'model': args.model,
        'use_ewc': args.use_ewc,
        'batch': args.batch,
        'epoch': args.epoch,
        'slide_win': args.slide_win,
        'slide_stride': args.slide_stride,
        'comment': args.comment,
        # 'seed': args.random_seed,
        'decay': args.decay,
        'val_ratio': args.val_ratio,
        'dim': args.dim,
        'out_layer_num': args.out_layer_num,
        'out_layer_inter_dim': args.out_layer_inter_dim,
        'topk': args.topk,
        'drop_prob': args.drop_prob,
        'hidden_dim': args.hidden_dim,
        'num_heads': args.num_heads,
        'num_layers': args.num_layers,
        'd_model': args.d_model,
        'sensor_num': args.sensor_num,
        'kernel_length': args.kernel_length,
        'fc1_size': args.fc1_size,
        'fc2_size': args.fc2_size
    }

    env_config = {
        'save_path': args.save_path_pattern,
        'dataset': args.dataset,
        'report': args.report,
        'device': args.device,
        'load_model_path': args.load_model_path
    }

    if model_name is not None and model_name in ['CNN', 'GDN', 'GRU', 'LSTM', 'LSTMVAE', 'RNN', 'MLP', 'Transformer']:
        train_config['model'] = model_name

    if dataset is not None:
        env_config['dataset'] = dataset

    main = Main(train_config, env_config, debug=False)
    main.run()


model_exp(model_name='LSTM')