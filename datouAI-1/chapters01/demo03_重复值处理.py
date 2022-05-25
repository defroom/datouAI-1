import pandas as pd

df = pd.DataFrame(data={'A':['a','b','a','c'],'B':[3,2,3,2]})
print(df)
# 判断重复数据记录
print(df.duplicated())
print(df.drop_duplicates())
print(df.drop_duplicates(['B'],keep='last'))