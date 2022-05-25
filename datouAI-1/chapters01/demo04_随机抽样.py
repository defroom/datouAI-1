import random
import numpy as np

data = np.loadtxt('../data/numpy_data_1.txt')
print(data.shape)
print(data[[1, 3, 5, 7],])
# 列表解析式
print([i for i in range(10)])
data_sample = data[random.sample([i for i in range(len(data))], 2000)]
print(data_sample[:10])
print(data_sample.shape)

# 分群代码如下，每个群体的采用参考上面代码
data = np.loadtxt('../data/numpy_data_2.txt')
label_y = np.unique(data[:, -1])
print(label_y)
sample_label = random.sample(set(label_y), 2)
print(sample_label)
