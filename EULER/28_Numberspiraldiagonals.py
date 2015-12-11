#https://www.hackerrank.com/contests/projecteuler/challenges/euler028/submissions/code/4341203
def g(L):
    n = (L-1) // 2
    return (16*n**3 + 30*n**2 + 26*n + 3) // 3

cases=int(raw_input())
for j in range(cases):
    N = int(raw_input())
    print g(N)%(10**9+7)