import torch.nn as nn
from industrial_time_series_analysis.Forecast.forecast_continuous_learning.util.env import *
import math
import torch.nn.functional as F


def get_batch_edge_index(org_edge_index, batch_num, node_num):  # 获取batch的边索引
    # org_edge_index:(2, edge_num)
    edge_index = org_edge_index.clone().detach()  # 硬clone并取消计算图连接
    edge_num = org_edge_index.shape[1]  # 获取边数量
    batch_edge_index = edge_index.repeat(1, batch_num).contiguous()  # 将边索引按批次数量进行复制且保证其在内存中是连续的

    for i in range(batch_num):
        batch_edge_index[:, i * edge_num:(i + 1) * edge_num] += i * node_num  # 通过偏移量将每个batch的边索引逐次偏移，其偏移量为节点数量

    return batch_edge_index.long()


class OutLayer(nn.Module):  # 输出层定义（MLP）
    def __init__(self, in_num, node_num, layer_num, inter_num=512):  # 输入特征数in_num 节点数node_num 层数layer_num中间特征数inter_num
        super(OutLayer, self).__init__()

        modules = []  # 创建空列表存储模型

        for i in range(layer_num):  #
            # last layer, output shape:1
            if i == layer_num - 1:  # 判断是否为最后一层
                modules.append(nn.Linear(in_num if layer_num == 1 else inter_num,
                                         1))  # 最后一层：如果该网络只有一层，那么(in_num,1）,如果不是的话（inter_num,1）
            else:
                layer_in_num = in_num if i == 0 else inter_num  # 如果是第一层 输入为in_num,如果是中间层，输入为inter_num
                modules.append(nn.Linear(layer_in_num, inter_num))  # 创建线性层
                modules.append(nn.BatchNorm1d(inter_num))  # 添加归一化层
                modules.append(nn.ReLU())  # 添加激活函数

        self.mlp = nn.ModuleList(modules)  # 转化为ModuleList

    def forward(self, x):  # 前向传播
        out = x

        for mod in self.mlp:  # 对层级进行遍历
            if isinstance(mod, nn.BatchNorm1d):  # 如果是归一化层，维度转置并归一化
                out = out.permute(0, 2, 1)
                out = mod(out)
                out = out.permute(0, 2, 1)
            else:
                out = mod(out)  # 计算

        return out


class GNNLayer(nn.Module):
    def __init__(self, in_channel, out_channel, inter_dim=0, heads=1, node_num=100):
        super(GNNLayer, self).__init__()

        self.gnn = GraphLayer(in_channel, out_channel, inter_dim=inter_dim, heads=heads,
                              concat=False)  # 使用图卷积层，如果改DGL应该是改这里

        self.bn = nn.BatchNorm1d(out_channel)  # 批量归一化层
        self.relu = nn.ReLU()  # ReLu激活函数
        self.leaky_relu = nn.LeakyReLU()  # leakyReLU激活函数

    def forward(self, x, edge_index, embedding=None, node_num=0):
        out, (new_edge_index, att_weight) = self.gnn(x, edge_index, embedding,
                                                     return_attention_weights=True)  # 输入x 边索引 节点嵌入 和节点数量 进行图卷积 这里直接调用gnn的forward
        self.att_weight_1 = att_weight  # 保存新的权重
        self.edge_index_1 = new_edge_index  # 保存新的边嵌入

        out = self.bn(out)  # 批量归一化

        return self.relu(out)  # 使用relu激活函数,原文中公式(5) 外壳


class GDN(nn.Module):
    def __init__(self, edge_index_sets, node_num, dim=64, out_layer_inter_dim=256, input_dim=10, out_layer_num=1,
                 topk=20, prior_graph=True):  # GDN模型的主体部分,初始化包括各种数据

        super(GDN, self).__init__()  # 调用父类初始化函数

        self.edge_index_sets = edge_index_sets  # 初始化边连接情况，这里是一个一维的list

        device = get_device()  # 获取计算设备信息

        edge_index = edge_index_sets[0]  # 获取每个阶段针对与边的连接关系，因为只有一层，所以是复制操作？

        embed_dim = dim  # 获取表示维数dim
        self.embedding = nn.Embedding(node_num, embed_dim)  # 对于每个节点使用dim维向量对节点进行表示（这一应该是编码层）
        self.bn_outlayer_in = nn.BatchNorm1d(embed_dim)  # 对数据根据结点的表示向量的大小进行批量规范化（这一层应该是输出层？）

        edge_set_num = len(edge_index_sets)  # 因为是一层，所以这里为1，但是是不是如果换数据集就会改？
        self.gnn_layers = nn.ModuleList([
            GNNLayer(input_dim, dim, inter_dim=dim + embed_dim, heads=1) for i in range(edge_set_num)
            # 对GNN层进行初始化，根据边的数量调整GNN的相应参数
        ])

        self.node_embedding = None
        self.topk = topk
        self.learned_graph = None

        self.out_layer = OutLayer(dim * edge_set_num, node_num, out_layer_num,
                                  inter_num=out_layer_inter_dim)  # 针对输出层进行参数初始化。

        self.cache_edge_index_sets = [None] * edge_set_num  # 这一部分为edge和set索引的缓存
        self.cache_embed_index = None  # 创建编码缓存
        self.prior_graph = prior_graph

        self.dp = nn.Dropout(0.2)  # 调整dropout比率

        self.init_params()

    def init_params(self):
        nn.init.kaiming_uniform_(self.embedding.weight, a=math.sqrt(5))  # 使用kaiming均值分布对神经网络进行初始化

    def forward(self, data, org_edge_index):  # 前向传播函数

        x = data.clone().detach()  # 由于这里的x需要重复使用，因此使用.clone().detach()操作拷贝副本并离开计算图
        xx = torch.tensor(x)
        # print('输入x',x,x.shape)
        # print('self.edge_index_sets', self.edge_index_sets)
        # print('self.cache_embed_index', self.cache_embed_index)
        edge_index_sets = self.edge_index_sets  # 传递

        device = data.device  # 传递设备参数

        batch_num, node_num, all_feature = x.shape  # 保存x的形状信息，batch数量、节点数量、数据
        # print('batch_num',batch_num,'node_num',batch_num,'all_feature',all_feature,)
        x = x.view(-1, all_feature).contiguous()  # 使用.view()改变x的形状，其中每一行表示每个节点的向量

        gcn_outs = []  # 存储GNN层输出
        for i, edge_index in enumerate(edge_index_sets):  # 这个由于是多个batch一起训练，因此在训练的时候要判断每个batch的状态？也不对 这里这个循环到底是干啥的
            edge_num = edge_index.shape[1]  # 所以这里是两层，没问题，这是获取所有连接的边的数量
            cache_edge_index = self.cache_edge_index_sets[i]  # 获取缓存中的边索引

            if cache_edge_index is None or cache_edge_index.shape[
                1] != edge_num * batch_num:  # 做一个判断，检查缓存中的边索引是否存在或当前边数量不匹配
                self.cache_edge_index_sets[i] = get_batch_edge_index(edge_index, batch_num, node_num).to(
                    device)  # 获取batch的边索引

            batch_edge_index = self.cache_edge_index_sets[i]  # 获取batch的边索引
            # print('edge_index1222111', edge_index)
            # print('batch_edge_index111111121',batch_edge_index)
            # print('第{i}次',i)

            all_embeddings = self.embedding(torch.arange(node_num).to(device))  # 调用embeding层给每一个节点进行编码

            weights_arr = all_embeddings.detach().clone()  # 权重参数使用对节点的编码
            all_embeddings = all_embeddings.repeat(batch_num, 1)  # 根据batch的数量对编码进行复制，每一个batch对于一组编码

            weights = weights_arr.view(node_num, -1)  # 将节点表示向量根据节点个数转化为二维矩阵

            cos_ji_mat = torch.matmul(weights, weights.T)  # 计算根据embed而生成的结点之间的相似性，这里用的是cos相似性？
            normed_mat = torch.matmul(weights.norm(dim=-1).view(-1, 1),
                                      weights.norm(dim=-1).view(1, -1))  # 计算节点表示向量的归一化矩阵
            cos_ji_mat = cos_ji_mat / normed_mat  # 对节点相似性的关系进行归一化,原文中公式（2）
            # print('cos_ji_mat', cos_ji_mat,cos_ji_mat.shape)

            dim = weights.shape[-1]  # 检查embeding后的值的维度（embeding）
            topk_num = self.topk  # 取前k个关系
            # print('topk_num',topk_num)

            topk_indices_ji = torch.topk(cos_ji_mat, topk_num, dim=-1)[1]  # 这里取得为前k个关系，获取topk在原数组的标号，其实是k-1个原文中公式(3)
            # print('topk_indices_ji',topk_indices_ji,topk_indices_ji.shape)

            self.learned_graph = topk_indices_ji  # 保存学习的图结构
            # print(self.learned_graph)

            gated_i = torch.arange(0, node_num).T.unsqueeze(1).repeat(1, topk_num).flatten().to(device).unsqueeze(
                0)  # 计算GAT的边索引？这里是node_nimxtopk_num的行向量
            # print('gated_i:',gated_i,gated_i.shape)
            gated_j = topk_indices_ji.flatten().unsqueeze(0)  # 将topk的数据根据0维展开，展开为node_numxtop_k的1维向量，为图注意力机制中的注意力权重
            # print('gated_j',gated_j,gated_j.shape)
            gated_edge_index = torch.cat((gated_j, gated_i), dim=0)  # 原文中公式7 将gi和gj进行拼接，构成完整的边索引
            # print('gated_edge_index',gated_edge_index,gated_edge_index.shape)
            # print('批次数量：',batch_num)
            # print('gated_edge_index', gated_edge_index, 'gated_edge_index.shape',
            #       gated_edge_index.shape)
            batch_gated_edge_index = get_batch_edge_index(gated_edge_index, batch_num, node_num).to(
                device)  # 将计算后的边索引按照批次数量进行复制
            # print('batch_gated_edge_index', batch_gated_edge_index,'batch_gated_edge_index.shape', batch_gated_edge_index.shape)
            # baatt = torch.tensor(batch_gated_edge_index)
            # print('baatt', baatt, 'baatt.shape',baatt.shape)
            #
            input_batch_edge_index = batch_edge_index if not self.prior_graph else batch_gated_edge_index
            # BAATT = torch.tensor(input_batch_edge_index)
            # print('BAATT', BAATT, 'BAATT.shape', BAATT.shape)
            # print('input_batch_edge_index:', input_batch_edge_index, 'input_batch_edge_index.shape', input_batch_edge_index.shape)
            # print('all_embeddings:', all_embeddings, 'all_embeddings.shape', all_embeddings.shape)
            gcn_out = self.gnn_layers[i](x, input_batch_edge_index, node_num=node_num * batch_num,
                                         embedding=all_embeddings)  # 调用GNN进行计算，得到输出
            #

            gcn_outs.append(gcn_out)  # 将当前GNN层输入添加到列表中

        x = torch.cat(gcn_outs, dim=1)
        x = x.view(batch_num, node_num, -1)  # 将输出的特征矩阵进行形状变换，恢复为原始的数据形状

        indexes = torch.arange(0, node_num).to(device)  # 索引向量，计算输出层的权重
        out = torch.mul(x, self.embedding(indexes))  # 原论文式(9)，特征矩阵与节点嵌入进行元素级乘法，加强表达

        out = out.permute(0, 2, 1)  # 进行维度变换，保证节点特征维度在最后
        out = F.relu(self.bn_outlayer_in(out))  # 对输出进行批量归一化并使用relu激活函数计算
        out = out.permute(0, 2, 1)  # 恢复输出维度

        out = self.dp(out)  # dropout
        out = self.out_layer(out)  # 导入输出层进行预测
        out = out.view(-1, node_num)  # 形状变换

        return out

import torch
from torch.nn import Parameter, Linear, Sequential, BatchNorm1d, ReLU
import torch.nn.functional as F
from torch_geometric.nn.conv import MessagePassing
from torch_geometric.utils import remove_self_loops, add_self_loops, softmax

from torch_geometric.nn.inits import glorot, zeros
import time
import math


class GraphLayer(MessagePassing):
    def __init__(self, in_channels, out_channels, heads=1, concat=True,
                 negative_slope=0.2, dropout=0, bias=True, inter_dim=-1,
                 **kwargs):  # in/out_channels为输入输出通道数，head为多头注意力机制头数
        super(GraphLayer, self).__init__(aggr='add', **kwargs)

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.heads = heads
        self.concat = concat
        self.negative_slope = negative_slope
        self.dropout = dropout

        self.__alpha__ = None

        self.lin = Linear(in_channels, heads * out_channels,
                          bias=False)  # 线性变换层 in_channels本质是上是滑动窗口的大小，out_channel是给节点数据进行编码的dim，这一层本质上就是将数据进行扩维，方便后续计算

        self.att_i = Parameter(torch.Tensor(1, heads, out_channels))
        self.att_j = Parameter(torch.Tensor(1, heads, out_channels))
        self.att_em_i = Parameter(torch.Tensor(1, heads, out_channels))
        self.att_em_j = Parameter(torch.Tensor(1, heads,
                                               out_channels))  # 注意力学习系数向量，在本算法中注意力机制的学习系数向量对于每一个node而言是相同的。 att为针对节点的注意力参数 att_em是边的注意力参数

        if bias and concat:
            self.bias = Parameter(torch.Tensor(heads * out_channels))
        elif bias and not concat:
            self.bias = Parameter(torch.Tensor(out_channels))
        else:
            self.register_parameter('bias', None)  # 根据设置（是否有偏置和拼接）确定偏置参数

        self.reset_parameters()

    def reset_parameters(self):
        glorot(self.lin.weight)
        glorot(self.att_i)
        glorot(self.att_j)

        zeros(self.att_em_i)
        zeros(self.att_em_j)

        zeros(self.bias)  # 初始化参数

    def forward(self, x, edge_index, embedding, return_attention_weights=False):  # 前向传播函数,这里edge_index是前k个节点的连接关系
        """"""
        if torch.is_tensor(x):  # x的形状为[nodenum*batchnum,window_size]
            x = self.lin(x)  # 过全链接层将window_size转化成dim
            x = (x, x)
        else:
            x = (self.lin(x[0]), self.lin(x[1]))

        edge_index, _ = remove_self_loops(edge_index)  # 去除连接中包含的自环边
        edge_index, _ = add_self_loops(edge_index,
                                       num_nodes=x[1].size(self.node_dim))  # 在连接中根据节点数量添加自环边

        out = self.propagate(edge_index, x=x, embedding=embedding, edges=edge_index,
                             return_attention_weights=return_attention_weights)  # 使用消息传递机制更新节点（调用messgae） 输出是[node_num*(topk-1), heads,dim]

        if self.concat:
            out = out.view(-1, self.heads * self.out_channels)  # 将out转换为形状为batch_size,head*out_channels形状
        else:
            out = out.mean(dim=1)  # 求在第一个维度上均值

        if self.bias is not None:  # 加入偏置
            out = out + self.bias

        if return_attention_weights:
            alpha, self.__alpha__ = self.__alpha__, None  # 清空注意力权重并返回
            return out, (edge_index, alpha)
        else:
            return out

    def message(self, x_i, x_j, edge_index_i, size_i,
                embedding,
                edges,
                return_attention_weights):  # 消息传递机制更新节点

        x_i = x_i.view(-1, self.heads, self.out_channels)
        x_j = x_j.view(-1, self.heads, self.out_channels)  # 修改多头注意力机制，将其作为第二个维度

        if embedding is not None:  # 如果存在嵌入特征
            embedding_i, embedding_j = embedding[edge_index_i], embedding[
                edges[0]]  # 提取原节点和目标节点特征嵌入[batch_num*node_num*topk,embeding_dim]
            embedding_i = embedding_i.unsqueeze(1).repeat(1, self.heads, 1)
            embedding_j = embedding_j.unsqueeze(1).repeat(1, self.heads, 1)  # 根据多头注意力机制扩展维度

            key_i = torch.cat((x_i, embedding_i), dim=-1)
            key_j = torch.cat((x_j, embedding_j), dim=-1)  # 拼接连接嵌入向量和节点信息向量，原文公式（6）

        cat_att_i = torch.cat((self.att_i, self.att_em_i), dim=-1)
        cat_att_j = torch.cat((self.att_j, self.att_em_j), dim=-1)  # 对上文中的注意力权重参数进行拼接

        alpha = (key_i * cat_att_i).sum(-1) + (key_j * cat_att_j).sum(-1)  # 计算每个节点与其邻居之间的注意力权重，求内积

        alpha = alpha.view(-1, self.heads, 1)  # 重塑？

        alpha = F.leaky_relu(alpha, self.negative_slope)  # 以上三行代码为论文中公式（7）
        self.node_dim = 0  # 这句是为了避免冲突？但是为什么是0
        alpha = softmax(alpha, edge_index_i, num_nodes=size_i)  # 对注意力权重使用softmax进行归一化 对应源论文中公式（8）

        if return_attention_weights:
            self.__alpha__ = alpha

        alpha = F.dropout(alpha, p=self.dropout, training=self.training)  # dropout

        return x_j * alpha.view(-1, self.heads, 1)  # 返回计算后的xi，对应原文公式(5)中括号内部分

    def __repr__(self):  # 返回当前信息
        return '{}({}, {}, heads={})'.format(self.__class__.__name__,
                                             self.in_channels,
                                             self.out_channels, self.heads)