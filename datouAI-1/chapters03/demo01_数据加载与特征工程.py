from sklearn.datasets import load_boston

df = load_boston()
print(type(df),df.keys())

X = df['data']
y = df['target']
print(X)
print(X.shape,y.shape)


columns = df['feature_names']
import matplotlib.pyplot as plt


# for i in range(X.shape[1]):
#     plt.scatter(X[:,i],y)
#     plt.title(columns[i])
#     plt.show()

import numpy as np
print(f'max:{np.max(y)},min:{np.min(y)}')

X = X[y<50.0]
y = y[y<50.0]

print(X.shape,y.shape)

plt.scatter(X[:,5],y)
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
print(X_train.shape,y_train.shape)
print(X_test.shape,y_test.shape)