#https://www.hackerrank.com/contests/projecteuler/challenges/euler022/submissions/code/4338006
import string


def query(name,data): 
	if name in data:
		ind=data.index(name)+1
		sum = 0
		for elem in list(name):
			sum+=Alphabet.index(elem)+1
		print ind*sum

Alphabet = list(string.uppercase)
data=[]

num_names=int(raw_input())
for i in range(num_names):
    name = raw_input()
    data.append(name)
data.sort()

num_queries=int(raw_input())

for i in range(num_queries):
    name = raw_input()
    query(name,data)

