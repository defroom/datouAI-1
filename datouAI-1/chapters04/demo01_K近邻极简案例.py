import pandas as pd

df = pd.read_excel("../data/葡萄酒.xlsx")
df.info()
print(df.head(n=5))
# 获取特征值与目标值
# X_train = df[['酒精含量(%)','苹果酸含量(%)']]
X_train = df.drop(labels=['原始样本', '分类'], axis=1)
y_train = df['分类']
# print(X_train)
# print(y_train,type(y_train))

# 导入knn分类算法
from sklearn.neighbors import KNeighborsClassifier as KNN

knn = KNN(n_neighbors=3)
knn.fit(X_train, y_train)
# 模拟数据进行测试
X_test = [[7, 1]]
# 所有分类算法本质输出的都是类别的概率
print(knn.predict_proba(X_test))

y_pred = knn.predict(X_test)
print(y_pred)
