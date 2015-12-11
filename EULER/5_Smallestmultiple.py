#https://www.hackerrank.com/contests/projecteuler/challenges/euler005/submissions/code/2542664
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
primes=[2,3,5,7,11,13,17,19,23,29,31,37]
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
for tc in range(int(input())):
    num=1
    fact=defaultdict(int)
    for i in range(2,int(input())+1):
        if i in primes:
            fact[i]+=1
        else:
            ls=prime_factors(i)
            for k,v in ls.iteritems():
                if v>fact[k]:
                    fact[k]=v
            
    for k,v in fact.iteritems():
        num=num*(k**v)
    print num