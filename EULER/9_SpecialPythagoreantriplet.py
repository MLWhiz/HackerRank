#https://www.hackerrank.com/contests/projecteuler/challenges/euler009/submissions/code/2542871
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from collections import defaultdict
pt=[]
for a in range(1,3000):
    for b in range(a,3000):
        c=math.sqrt(a**2+b**2)
        if c%1==0:
            c = int(c)
            #print (a,b,c)
            pt.append([a,b,c])
ptdict={}
for elem in pt:
    a,b,c=elem
    #print elem
    key=a+b+c
    mul=a*b*c
    if key in ptdict and key<=3000:
        if ptdict[key]<mul:
            ptdict[key]=mul
    elif key<=3000:
        ptdict[key]=mul
#print ptdict
    
for i in range(input()):
    try: 
        print ptdict[input()]
    except:
        print -1