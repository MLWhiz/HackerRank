#https://www.hackerrank.com/contests/projecteuler/challenges/euler020/submissions/code/4337889
fact_list = [0]*1001
def fact(n):
    if n ==1 or n==0:
        return 1
    if fact_list[n]!=0:
        return fact_list[n]
    fact_list[n] = n*fact(n-1)
    return fact_list[n]


for i in range(0,1001):
    a = fact(i)

fact_list[0]=1
fact_list = [sum([int(y) for y in list(str(x))]) for x in fact_list]

cases=int(raw_input())
for i in range(cases):
    num = int(raw_input())
    print fact_list[num]