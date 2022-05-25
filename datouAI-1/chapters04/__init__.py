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
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=1,test_size=0.5,stratify=y)
# print(y_train.value_counts())
# print(y_test.value_counts())
from sklearn.preprocessing import StandardScaler
std = StandardScaler()
X_train = std.fit_transform(X_train)
X_test = std.transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
from sklearn.model_selection import GridSearchCV
gc = GridSearchCV(estimator=knn,param_grid={'n_neighbors':[3,5],'weights':['uniform','distance']},cv=5)
gc.fit(X_train,y_train)
# 网格搜索与交叉验证的结果如下:
# 交叉验证与网格搜索相关结果如下：
print('平均最优训练分数',gc.best_score_)
print('平均最优训练分数',gc.score(X_test,y_test))
print('-'*100)
