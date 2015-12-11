# https://www.hackerrank.com/challenges/predicting-office-space-price/submissions/code/10573253

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

data =str(raw_input())
m, n=data.split(" ")
m=int(m)
n=int(n)
X=[]
Y=[]
for i in range(0,n):
    data2 = str(raw_input()).split(" ")
    data = [float(x) for x in data2]
    X.append(data[:m])
    Y.append(data[m])
# Now I have to do linear regression
poly = PolynomialFeatures(degree=3)
X = np.matrix(X)
X=poly.fit_transform(X)
clf = linear_model.LinearRegression()
clf.fit(X,Y)

'''
Xt=np.matrix.transpose(X)
Fin=(linalg.inv(Xt.dot(X)).dot(Xt)).dot(Y)
#print Fin
'''
n = int(raw_input())
for i in range(0,n):
    data2 = str(raw_input()).split(" ")
    data = np.matrix([[float(x) for x in data2]])
    data=poly.transform(data)
    print clf.predict(data)[0]    
