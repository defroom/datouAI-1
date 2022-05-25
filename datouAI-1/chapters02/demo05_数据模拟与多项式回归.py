import numpy as np
import matplotlib.pyplot as plt
# 模拟X与y
x = np.random.uniform(-3,3,size=100)
print(x.shape,x)
X = x.reshape(-1,1)
y = 0.5*x**2 + x + 2 + np.random.normal(0,1,100)
print(y.shape)

plt.scatter(x,y)
plt.show()

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)
print(f'权重为:{lr.coef_},偏置为:{lr.intercept_}')
y_predict = lr.predict(X)
plt.scatter(x,y,color='b')
# 可视化预测值
plt.plot(x,y_predict,color='r')
plt.show()

# 构建多项式线性回归
X2= np.hstack([X**2,X])
print(X2.shape)
lr.fit(X2,y)
# y = w*x**2 + w*x + b
print(f'权重为:{lr.coef_},偏置为:{lr.intercept_}')
y_predict = lr.predict(X2)

plt.scatter(x,y,color='g')
# 可视化预测值
# plt.plot(x,y_predict,color='r')
plt.plot(x[np.argsort(x)],y_predict[np.argsort(x)],color='r')
plt.show()