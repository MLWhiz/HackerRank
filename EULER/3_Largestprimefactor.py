#https://www.hackerrank.com/contests/projecteuler/challenges/euler003/submissions/code/2542575
def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

for i in range(int(input())):
    pfs = prime_factors(int(input()))
    print max(pfs) # The largest element in the prime factor list