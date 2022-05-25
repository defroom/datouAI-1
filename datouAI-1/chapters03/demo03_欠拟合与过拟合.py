from sklearn.datasets import load_boston

df = load_boston()

X = df['data']
y = df['target']

# X = X[y<50.0]
# y = y[y<50.0]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(degree=3,include_bias=False,interaction_only=False)
X_train = pf.fit_transform(X_train)
# print(len(pf.get_feature_names()),pf.get_feature_names())

from sklearn.preprocessing import StandardScaler
std_x = StandardScaler()
std_x.fit(X_train)
X_train = std_x.transform(X_train)

std_y = StandardScaler()
y_train = std_y.fit_transform(y_train.reshape(-1, 1))



from sklearn.linear_model import LinearRegression,Ridge
lr = Ridge(alpha=0.8)
lr.fit(X_train,y_train)

X_test = pf.transform(X_test)
X_test = std_x.transform(X_test)
y_test = std_y.transform(y_test.reshape(-1, 1))
# 训练集:1.0,测试集score:-16.444857865836223
# 训练集:0.9511508420004483,测试集score:0.9332913489378397
print(f'权重为:{lr.coef_},偏置为:{lr.intercept_}')
print(f'训练集:{lr.score(X_train,y_train)},测试集score:{lr.score(X_test,y_test)}')

