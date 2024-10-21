import numpy as np
import pandas as pd
from .functions import multi_to_one, model_predict


'''
算法说明：通用回归时序数据神经网络算法。多特征输入，单特征输出。支持多种神经网络模型。
        处理流程为：数据标准化，自动分段数据构造训练集和测试集，模型训练，模型测试。
        
具体输入输出说明：
举例来说，假设原始数据为
[[1, 2, 3, 4],
 [2, 3, 4, 5],
 [3, 4, 5, 6],
 [4, 5, 6, 7],
 [5, 6, 7, 8],
 ......]
 其中，第一列为模型要预测的特征，后三列为预测使用的特征。而且设定使用3个时间点预测后2个时间点
 那么，对于第一条数据，输入模型的数据为：
 [[2, 3, 4],
 [3, 4, 5],
 [4, 5, 6]]
 模型的输出应该为（也就是ground truth）:
[[4],
 [5]]
 此外，在进行数据集分段时，每两条输入数据“没有重合部分”。也就是使用滑动窗口对数据进行分段时的步长等于输入时间点个数

数据预处理：输入已经预处理的excel文件。需要先对原始数据进行预处理，比如删除时间戳，对离散值进行编码等
         举例来说，原始数据集见Steel_industry_data.xlsx，预处理好的示例文件见steel_power_train.xlsx，
         这是一个预测钢铁功率的数据集
        
算法输入：
        data_path:excel文件路径
        model_name:使用的神经网络模型的名称，可选模型：InceptionTimePlus, LSTMPlus, FCNPlus, RNNPlus, RNN_FCNPlus, TSTPlus
        predict_fea_index:要预测的特征在第几列，默认为0，即第一列
        total_epoch:训练轮次
        save_path:模型保存路径
        window_length:在预测时，输入模型多少个数据点
        horizon:预测未来多少个数据点

算法输出：
        训练好的模型文件，保存在model文件夹中
        训练过程loss曲线
'''

def timeseries_regression(data_path, predict_fea_index, model_name, total_epoch, window_length, horizon):
    df = pd.read_excel(data_path)
    X = np.array(df.values, dtype=float)
    multi_to_one(X, predict_fea_index, model_name, total_epoch, window_length, horizon)


'''
在训练好模型后，可以使用predict函数对新数据进行预测。新数据同样为excel格式，见steel_power_predict.xlsx
新数据只包含输入特征

算法输入：
        data_path:预测使用的excel文件路径
        model_name:使用的神经网络模型的名称，和训练时的模型应保持一致
        save_path:测试模型的保存路径
        window_length:在预测时，输入模型多少个数据点。和训练时的参数应该一致
        horizon:预测未来多少个数据点。和训练时的参数应该一致
'''
def timeseries_predict(test_data_path, model_name, window_length, horizon):
    # 数据格式转换
    df = pd.read_excel(test_data_path)
    test_X = np.array(df.values, dtype=float)
    test_X = np.swapaxes(test_X, axis1=0, axis2=1)
    test_X = np.expand_dims(test_X, axis=0)
    # 预测
    model_predict(test_X, model_name, window_length, horizon)


'''示例代码'''
if __name__ == '__main__':
    use_model_name = 'InceptionTimePlus'
    window_length = 10
    horizon = 5

    timeseries_regression(data_path='./input/steel_power_train.xlsx',
                   predict_fea_index=0,
                   model_name=use_model_name,
                   total_epoch=20,
                   window_length=window_length,
                   horizon=horizon)

    timeseries_predict(test_data_path='./input/steel_power_predict.xlsx',
            model_name=use_model_name,
            window_length=window_length,
            horizon=horizon)
