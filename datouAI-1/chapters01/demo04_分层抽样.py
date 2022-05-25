import random
import numpy as np
# 分层抽样
data = np.loadtxt('../data/numpy_data_2.txt')
each_sample_count = 100   # 定义每个分层的抽样数量
label_y = np.unique(data[:,-1])  # 获取分层的值域
print(label_y)
sample_data = []
sample_dict = {}
for y in label_y:
    sample_list = []    # 用于存储临时分层数据
    for row in data:
        if row[-1] == y:
            sample_list.append(row)   # 将数据加入分层数据中
    # 对当前类别数据集进行随机采样
    each_sample_data = random.sample(sample_list,each_sample_count)
    # 将抽样数据追加到总体样本集
    sample_data.extend(each_sample_data)
#     # 添加样本统计结果
    sample_dict[y] = len(each_sample_data)
print(sample_dict)
