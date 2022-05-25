import numpy as np
import pandas as pd
df = pd.DataFrame(data=np.random.randn(6,4),columns=list('ABCD'))
df.iloc[0:2,1] = np.nan
df.iloc[4,3] = np.nan
print(df)

# 判断缺失值
print(df.isnull())
print(df.isnull().any())
print(df.isnull().all())

print(df.dropna(axis=0)) # 直接丢弃有NA的行记录

print(df.fillna(value=0))
print(df.fillna({'B':1.1,'D':0.0}))
print(df.fillna(method='pad'))  # 用前面的值替换缺省值
print(df.fillna(method='backfill',limit=1))  # 用后面的值替换缺省值
print(df.fillna(value=df.mean()))  # 平均值填充