import numpy as np

# 等距抽样
data = np.loadtxt('../data/numpy_data_1.txt')
sample_count = 2000
record_count = data.shape[0]
width = record_count / sample_count  # 计算抽样间距
result_sample = []  # list 而非 ndarray
i = 0
# 当样本量小于指定抽样数据并且索引在有效范围内时
while len(result_sample) < sample_count and i * width < record_count:
    result_sample.append(data[int(i * width)]) # 新增样本
    i=i + 1
result_sample = np.array(result_sample)
print(result_sample[:10])
print(result_sample.shape)