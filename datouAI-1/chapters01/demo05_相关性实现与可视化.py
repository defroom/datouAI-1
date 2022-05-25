import numpy as np

data = np.loadtxt("../data/numpy_data_3.txt",delimiter='\t')
x = data[:,:-1]
matrix = np.corrcoef(x,rowvar=False)  # 相关性分析
print(matrix.round(2))

import pandas as pd
df = pd.DataFrame(data=x)
print(df.corr().round(2))

# 对所有的标签和特征两两显示其相关性的热力图(heatmap)
# annot = True 在每个方格显示数值
import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(np.abs(matrix), cmap="YlGnBu", annot = True)
plt.xlabel('heatmap')
plt.show()