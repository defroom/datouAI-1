from sklearn.datasets import load_boston

# 1: 数据获取
X, y = load_boston(return_X_y=True)
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

pip_lr = Pipeline(steps=[('pf', PolynomialFeatures(degree=3, include_bias=False)), ('std', StandardScaler()),
                         ('lr', Ridge(alpha=0.8))])
pip_lr.fit(X_train, y_train)
print(f'训练集:{pip_lr.score(X_train, y_train)},测试集score:{pip_lr.score(X_test, y_test)}')
# 7: Pipeline 保存与加载使用
