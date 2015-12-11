#https://www.hackerrank.com/challenges/quora-answer-classifier/submissions/code/10573827
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=str(raw_input()).split(" ")
D=[]
y=[]
for i in range(0,int(n)):
    data=(raw_input()).split(" ")
    id=data[0]
    if int(data[1])==1:
        target=1
    else:
        target=0
    y.append(target)
    d=[]
    for elem in data[2:]:
        _,val=elem.split(":")
        d.append(float(val))
    D.append(d)
#print D
from sklearn.ensemble import RandomForestClassifier


clf = RandomForestClassifier(criterion="entropy",n_estimators=13)
clf.fit(D,y)

n=int(raw_input())
for i in range(0,n):
    data=(raw_input()).split(" ")
    id=data[0]
    d=[]
    for elem in data[1:]:
        _,val=elem.split(":")
        d.append(float(val))
    ypred=clf.predict(d)[0]
    if ypred ==0:
        print id+" -1"
    else:
        print id+" +1"