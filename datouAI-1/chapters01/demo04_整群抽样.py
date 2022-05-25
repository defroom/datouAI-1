import numpy as np
import random
# 分群代码如下，每个群体的采用参考上面代码
data = np.loadtxt('../data/numpy_data_2.txt')
label_y = np.unique(data[:,-1])
print(label_y)
sample_label = random.sample(set(label_y),2)
print(sample_label)