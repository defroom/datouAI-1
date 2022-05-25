import pandas as pd

df = pd.read_csv("../data/numpy_data_4.txt",sep="\t",names=['id','amount','income','datetime','age'])
print(df.head(n=3))
# 日期序列化，把时间转化为周为基本单位
df['datetime'] = list(map(pd.to_datetime,df['datetime']))
print(df.info())
df['datetime'] = [i.weekday() for i in df['datetime']]
print(df.head(5))

from sklearn.cluster import KMeans
# 采用聚类实现离散化
data = df['amount']
data_reshape = data.values.reshape(data.shape[0],1)
# 机器学习训练的数据首先要是2维
model_kmeans = KMeans(n_clusters=4)
kmeans_result = model_kmeans.fit_predict(data_reshape)
print(kmeans_result)
df['amount2'] = kmeans_result
print(df)


def cluValue(val):
    if val > 7500:
        return 4
    elif val > 5000:
        return 3
    elif val > 2500:
        return 2
    else:
        return 1

df['amount3'] = df['amount'].map(cluValue)
print(df)