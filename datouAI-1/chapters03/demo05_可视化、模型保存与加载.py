from sklearn.datasets import load_boston
# 1: 数据获取
X,y = load_boston(return_X_y=True)
# 2: 数据清洗预处理 (略)
# 3: 数据拆分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
# 4~6: 特征工程，模型训练，调优 (Pipeline)
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
# Pipeline构建机器学习工作流程:
from sklearn.pipeline import Pipeline
pip_lr = Pipeline(steps=[('pf',PolynomialFeatures(degree=3,include_bias=False)),('std',StandardScaler()),('lr',Ridge(alpha=0.8))])
pip_lr.fit(X_train,y_train)
from sklearn.metrics import r2_score
y_pred = pip_lr.predict(X_test)
print(f'r2_score: {r2_score(y_test,y_pred)}')
print(f'训练集:{pip_lr.score(X_train,y_train)},测试集score:{pip_lr.score(X_test,y_test)}')
# 7: Pipeline 保存与加载使用

import numpy as np
import matplotlib.pyplot as plt  # 通过左边搜索
# def plot(*args, scalex=True, scaley=True, data=None, **kwargs)
plt.plot(np.arange(len(y_test)),y_test,color='k',label='true y')
plt.plot(np.arange(len(y_pred)),y_pred,'g--',label='pred y')
# matplotlib.pyplot.legend(*args, **kwargs)
plt.legend()  # 也可以设置title的方向
# 可以吧Ridge替换为原来的LinearRegression 查看测试集误差大的可视化
plt.show()
# print(X_test.shape)
# from sklearn.linear_model import LinearRegression
# lr:LinearRegression = pip_lr.named_steps['lr']
# print(len(lr.coef_),lr.intercept_)
#
# res = 1 - (1-pip_lr.score(X_test,y_test)*(127-1))/(127-559-1)
# print(f'adj R为:{res}')

# 保存模型方便后续加载
import joblib
# import sklearn.externals.joblib  # 适合老版本
joblib.dump(pip_lr,'../data/pip_lr.pkl')
