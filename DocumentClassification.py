#https://www.hackerrank.com/challenges/document-classification/submissions/code/10577787
# Enter your code here. Read input from STDIN. Print output to STDOUT
documents=[]
target=[]
cnt=0
from sklearn.linear_model import PassiveAggressiveClassifier
with open("trainingdata.txt","rb") as infile:
    for line in infile:
        if cnt==0:
            cnt=1
            continue
        category=int(line[0:2])
        doc=line[2:]
        target.append(category)
        documents.append(doc)
from sklearn.feature_extraction.text import TfidfVectorizer
transformer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word',stop_words='english')
X = transformer.fit_transform(documents)
from sklearn.naive_bayes import MultinomialNB
clf = PassiveAggressiveClassifier(n_iter=50)
clf.fit(X, target)

n=int(raw_input())
for i in range(0,n):
    X=transformer.transform([raw_input()])
    print(clf.predict(X))[0]

