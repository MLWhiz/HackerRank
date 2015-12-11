#https://www.hackerrank.com/challenges/make-it-anagram/submissions/code/10601943
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
str1 = list(raw_input())
str2 = list(raw_input())

d1=defaultdict(int)
d2=defaultdict(int)
for elem in str1:
    d1[elem]+=1
for elem in str2:
    d2[elem]+=1
sum=0
keys = list('abcdefghijklmnopqrstuvwxyz')
for key in keys:
    try:
        sum+=abs(d1[key]-d2[key])
    except:
        pass
    
print sum
