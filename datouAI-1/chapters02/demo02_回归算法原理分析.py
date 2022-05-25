import numpy as np
# 矩阵的点乘
t1 = np.arange(8).reshape(2,4)
t2 = t1
print(t1)
print(t2)
print(t1 * t2)

# 矩阵乘法(非常重要)
# 3个样本4个特征
x = np.arange(12).reshape(3,4)
print(x)
# 权重数与样本的特征数相同
w = np.arange(4).reshape(4,1)
print(w)
# 1、当矩阵A的列数（column）等于矩阵B的行数（row）时，A与B可以相乘。
# 2、矩阵C的行数等于矩阵A的行数，C的列数等于B的列数。
# 3、乘积C的第m行第n列的元素等于矩阵A的第m行的元素与矩阵B的第n列对应元素乘积之和。
y_pred = np.dot(x,w)
print(y_pred,y_pred.shape)
# print(x@w)
print('-'*100)
# 预测值与真实值运算求误差
y_pred = np.array([1,2,3,4])
y_true = np.array([1,2,3,12])
print('mae:',np.average(np.abs(y_pred - y_true)),sep='')
from sklearn.metrics import mean_absolute_error
print(f'mae:{mean_absolute_error(y_true,y_pred)}')
# 均方(根)误差的实现 （如果误差分布不均衡则均方根误差会大于绝对值误差）
mse = np.average((y_pred - y_true)**2)
print(f'均方误差{mse},均方根误差{np.sqrt(mse)}')
from sklearn.metrics import mean_squared_error
print(f'均方根误差:{mean_squared_error(y_true,y_pred,squared=False)}')
