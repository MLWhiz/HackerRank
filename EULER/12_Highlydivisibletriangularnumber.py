#https://www.hackerrank.com/contests/projecteuler/challenges/euler012/submissions/code/2542995
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = defaultdict(int)
    d = 2
    while n > 1:
        while n % d == 0:
            factors[d]+=1
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors[n]+=1
            break
    return factors

def num_factor(num):
        factors=1
        for key,value in prime_factors(num).iteritems():
            factors*=(value+1)
        return factors

flag=True
n=1
d=[0]*1001
max_nf=0
i=0

while flag==True:
    tn = n*(n+1)/2
    nf = num_factor(tn)
    if nf>max_nf:
        try:
            for j in range(max_nf,nf):
                d[j]=tn
            max_nf=nf
        except:
            for j in range(max_nf,1001):
                d[j]=tn
            max_nf=nf

    n+=1
    if nf>1001:
        flag=False

        
for i in range(input()):
    print d[input()]