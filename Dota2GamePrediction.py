#https://www.hackerrank.com/challenges/dota2prediction/submissions/code/10578072
# Enter your code here. Read input from STDIN. Print output to STDOUT
file_loc="trainingdata.txt"
D=[]
y=[]
with open(file_loc,"rb") as infile:
    for line in infile:
        data=line.split(",")
        y.append(int(data[10])-1)
        d={}
        for i,elem in enumerate(data[0:10]):
            if i<5:
                d[elem]=1
            else:
                d[elem]=-1
        D.append(d)
#print D

from sklearn.feature_extraction import DictVectorizer
v = DictVectorizer(sparse=False)
X = v.fit_transform(D)
from sklearn import linear_model
clf=linear_model.LogisticRegression(C=0.1)
clf.fit(X,y)

n=int(raw_input())

for i in range(0,n):
    line=str(raw_input())
    data=line.split(",")
    d={}
    for i,elem in enumerate(data[0:10]):
        if i<5:
            d[elem]=1
        else:
            d[elem]=-1
    X=v.transform(d)
    print clf.predict(X)[0]+1