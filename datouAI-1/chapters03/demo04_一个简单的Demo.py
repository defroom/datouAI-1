from sklearn.datasets import load_boston

X,y = load_boston(return_X_y=True)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
# Pipeline构建机器学习工作流程:
from sklearn.pipeline import Pipeline
pip_lr = Pipeline(steps=[('std',StandardScaler()),('lr',LinearRegression())])
print(pip_lr.get_params())
pip_lr.fit(X_train,y_train)
std:StandardScaler = pip_lr.named_steps['std']
print(std.mean_)
lr:LinearRegression = pip_lr.named_steps['lr']
print(lr.coef_,lr.intercept_)
# 调用score
print('score:',pip_lr.score(X_test,y_test))

