# -*- coding:utf-8 -*-
"""
Name：PanYunJie
Date：2024-07-20
"""
import os
file_path = f"../data/steel/TRain/Task1(拉速1.2)/板柸1_1数据/train.csv"
if os.path.exists(file_path):
    print("文件存在")
    # 读取文件
else:
    print("文件不存在")

print("当前工作目录:", os.getcwd())