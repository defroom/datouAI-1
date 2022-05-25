import numpy as np
import pandas as pd

df = pd.read_excel("../data/葡萄酒.xlsx")
df.info()

X = np.array(df.iloc[:,1:3])
y = df['分类']
print(X,type(X))
print(y,type(y))

future_data = np.array([[7,1]])
print(future_data,type(future_data))
squre_diff = (X - future_data)**2
print(squre_diff)
# 每一行进行求和操作
distance = np.sum(squre_diff,axis=1) ** 0.5
print(distance)
# 把邻居按照距离从小到大排序(邻居的索引)
distance_index = np.argsort(distance)
print(distance_index)
k = 3
label_count = [] # 对邻居的类别进行统计操作
for i in range(k):
    # 从小到大寻找就近邻居对应的label标签
    label = y[distance_index[i]]
    label_count.append(label)

print(f'label_count:{label_count}')
# 近邻的类别数进行统计
from collections import Counter
value_count = Counter(label_count)
print(value_count)
top = value_count.most_common(1)
print(top)