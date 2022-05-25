# preprocessing包下面的__init__.py文件导入了MinMaxScaler类
from sklearn.preprocessing import MinMaxScaler
# 本质上就是调用了前面的公式,可以自己指定max,min范围默认0~1之间
mm = MinMaxScaler(feature_range=(0, 1))
data = [[90, 2, 10, 40],
         [60, 4, 15, 45],
         [75, 3, 13, 46]]

# rs = mm.fit_transform(data)
mm.fit(data)
rs = mm.transform(data)
print(rs)

# 采用标准化对之前的数据进行归一化处理
from sklearn.preprocessing import MinMaxScaler, StandardScaler
std = StandardScaler()
# 进行标准化之后的结果
data = std.fit_transform([[90, 2, 10, 40],
                          [60, 4, 15, 45],
                          [75, 3, 13, 46]])
# 原始数据每列的平均值
print(std.mean_)
# std.inverse_transform(data)

