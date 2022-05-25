from sklearn.preprocessing import PolynomialFeatures
import numpy as np
pf = PolynomialFeatures(degree=2,include_bias=False,interaction_only=False)
# [1,a,b,a**2,a*b,b**2]
data = np.array([[3,5]])
# pf.fit(data)
# res = pf.transform(data)
# print(res)
res = pf.fit_transform(data)
print(res)
