import joblib
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

pip_lr: Pipeline = joblib.load("../data/pip_lr.pkl")
lr: LinearRegression = pip_lr.named_steps['lr']
print(len(lr.coef_), lr.intercept_)
# 获取未来的数据使用模型进行预测
from sklearn.datasets import load_boston
X, y = load_boston(return_X_y=True)
print(pip_lr.score(X, y))
