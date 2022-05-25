import pandas as pd

df = pd.DataFrame(data={'A': [1, 120, 3, 5, 2, 12, 13], 'B': [12, 17, 31, 53, 22, 32, 43]})
print(df)
df_zscore = df.copy()  # 复制一个用来存储Z-score得分的数据框
cols = df.columns  # 获得数据框的列名
print(cols)
# http://blog.sina.com.cn/s/blog_72208a6a0101cdt1.html
# 箱型图
for col in cols:  # 循环读取每列
    df_col = df[col]  # 得到每列的值
    # 计算每列的Z-score得分(是一个数与平均数的差再除以标准差的过程)
    z_score = (df_col - df_col.mean()) / df_col.std()
    # z_score 值就是一个衡量方差的标准 或者说是 单位（unit）
    # 判断Z-score得分是否大于2.2,(此处2.2代表一个经验值)，如果是则是True，否则为False
    df_zscore[col] = z_score.abs() > 2.2
# #
print(df_zscore)  # 打印输出
# df_zscore['col1'] == True 的就能丢掉了
df_drop_outlier = df[df_zscore['A'] == False]
print(df_drop_outlier)
