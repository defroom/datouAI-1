import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/diabetes.csv")
df.info()
print(df.head(n=3))

print(df.groupby('Class').size())
sns.countplot(df['Class'],label='class count')
plt.show()

X = df.iloc[:,:8]
y = df.iloc[:,8]
print(f'X.shape:{X.shape},y.shape:{y.shape}')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=1)

from sklearn.preprocessing import StandardScaler
std = StandardScaler()
X_train = std.fit_transform(X_train)
X_test = std.transform(X_test)

# 通过KNN模型选择邻居
from sklearn.neighbors import KNeighborsClassifier,RadiusNeighborsClassifier
models = []
# 传统KNN只统计邻居类别数量(不考虑邻居的距离)
models.append(('knn',KNeighborsClassifier(n_neighbors=3)))
models.append(('knn with distance',KNeighborsClassifier(n_neighbors=3,weights='distance')))
# 靠半径来确定邻居,半径范围内有多少算多少
models.append(('knn with radius',RadiusNeighborsClassifier(radius=100)))

results = []
for name,model in models:
    model.fit(X_train,y_train)
    results.append((name,model.score(X_test,y_test)))

for i in range(len(results)):
    print(f'name:{results[i][0]},score:{results[i][1]}')

