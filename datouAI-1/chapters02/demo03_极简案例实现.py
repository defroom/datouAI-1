import pandas as pd

# 1: 数据的加载
df = pd.read_csv("../data/house.csv")
df.info()
print(df.head(n=3))
# 对于预测,分类需求需要区分X,y
y = df['price']
X = df.drop("price", axis=1)
print(X)
# 2: 数据预处理 (清洗、异常值...) 略
# 3: 把数据拆分训练集和测试集
# sklearn: 机器学习框架   tensorflow: 深度学习框架
from sklearn.model_selection import train_test_split

# X_train,y_train: 训练集特征值与目标值
# X_test,y_test: 测试集特征值与目标值
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
# 4：特征工程(略)
print(X_test)
print(y_test)
# 5: 根据需求选择合适的模型 (聚类、回归、分类)
from sklearn.linear_model import LinearRegression

lr = LinearRegression()  # 创建 训练
lr.fit(X_train, y_train)  # 思考: 训练的过程就是求权重和偏置的过程
print(f'权重为:{lr.coef_},偏置为:{lr.intercept_}')
# y = wx0 + wx1 + b
# 传入测试集数据
y_predict = lr.predict(X_test)
# 预测值与真实值之差就是模型的误差
from sklearn.metrics import mean_absolute_error

print(f'mae:{mean_absolute_error(y_test, y_predict)}')
