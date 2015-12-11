#https://www.hackerrank.com/contests/projecteuler/challenges/euler027/submissions/code/4340877
from math import sqrt

def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def prime_sieve(n):
    """
    Return a list of prime numbers from 2 to a prime < n. Very fast (n<10,000,000) in 0.4 sec.
    
    Example:
    >>>prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]

    Algorithm & Python source: Robert William Hanks
    http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
    """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


def compute(a,b,n):
    return n**2+a*n+b

def get_ans(n):
    max_a = 0
    max_b = 0
    max_primes = 0
    for a in range(-n,n+1):
        for b in prime_sieve(n+1):
            num_primes = 0
            x=0
            while is_prime(compute(a,b,x)):
                num_primes+=1
                x+=1
            if num_primes>max_primes:
                max_primes =num_primes
                max_a = a
                max_b = b
    return max_a,max_b

case = int(raw_input())
a,b = get_ans(case)
print a,b