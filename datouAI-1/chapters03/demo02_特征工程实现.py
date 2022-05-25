from sklearn.datasets import load_boston

df = load_boston()
print(type(df),df.keys())

X = df['data']
y = df['target']

X = X[y<50.0]
y = y[y<50.0]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)


from sklearn.preprocessing import StandardScaler

std_x = StandardScaler()

std_x.fit(X_train)
X_train = std_x.transform(X_train)
X_test = std_x.transform(X_test)

std_y = StandardScaler()

y_train = std_y.fit_transform(y_train.reshape(-1, 1))
y_test = std_y.transform(y_test.reshape(-1, 1))
print(std_x.mean_,std_y.mean_)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)

# 进行标准化的权重为:[[-0.10969204  0.11850349 -0.05705757  0.02498305 -0.19450083  0.27357803
#   -0.07102985 -0.34543005  0.27868882 -0.27897086 -0.23213106  0.07254337
#   -0.34382204]],偏置为:[1.56368208e-15]
# 训练集:0.7774747579071718,测试集score:0.7706603159213965


# 没有进行标准化权重为:[-1.04302296e-01  4.19243190e-02 -6.59513006e-02  7.91820851e-01
#  -1.31657098e+01  3.31593763e+00 -2.01134036e-02 -1.31252228e+00
#   2.57958621e-01 -1.33034453e-02 -8.87447562e-01  6.49284234e-03
#  -3.75138276e-01],偏置为:37.315844349457365
# 训练集:0.7774747579071717,测试集score:0.7706603159213965

print(f'权重为:{lr.coef_},偏置为:{lr.intercept_}')
print(f'训练集:{lr.score(X_train,y_train)},测试集score:{lr.score(X_test,y_test)}')
