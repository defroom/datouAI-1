import numpy as np

x=[1.1, 1.9, 3]
y=[5.0, 10.4, 14.6]
ex = (1.1+1.9+3)/3
ey = (5.0+10.4+14.6)/3
exy= (1.1 * 5.0 + 1.9 * 10.4 + 3 * 14.6) / 3
# 计算协方差公式
cov_x_y= exy - ex * ey  # 23.02-2×10=3.02
print(ex,ey,exy,cov_x_y)
# 计算皮尔逊系数
# r(X,Y)=Cov(X,Y)/((std(x) * std(y)) = 3.02 /(0.77×3.93) = 0.9979
print('std',np.std(x),np.sqrt(np.average((x - np.mean(x))**2)))
print('std',np.std(y))
print(cov_x_y / (np.std(x) * np.std(y)))
from scipy.stats import pearsonr
# 采用官方皮尔逊公式
corr = pearsonr(x,y)
print(corr)
print(np.corrcoef(x,y)) # 相关性分析
