import numpy as np
import matplotlib.pyplot as plt

print(np.random.rand(3, 4))
# 功能同上,参数传入格式不同
print(np.random.random(size=[3, 4]))
# 返回指定范围的整形
print(np.random.randint(low=2, high=10, size=10))

import numpy as np

np.random.seed(1)
# 标准正态分布平均数μ=0，对应着整个分布的中心centre
# 标准差σ=1, 此概率分布的标准差(对应于分布的宽度,scale越大越矮胖,scale越小,越瘦高）
value = np.random.normal(loc=0.0, scale=1.0, size=50)
print(np.mean(value), np.std(value))
print(value)
# 绘制可省略

plt.hist(value, bins=100)
plt.show()

np.random.seed(1)
# # 从标准正态分布中返回样本
print(np.random.randn(50))
