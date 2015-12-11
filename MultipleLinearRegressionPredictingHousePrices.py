
#https://www.hackerrank.com/challenges/predicting-house-prices/submissions/code/10573205
import numpy as np
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
X = np.matrix(X)
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
    print clf.predict(data)[0]    


