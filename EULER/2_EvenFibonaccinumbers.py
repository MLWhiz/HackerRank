#https://www.hackerrank.com/contests/projecteuler/challenges/euler002/submissions/code/2542546
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    n1=1
    n2=2
    n3=0
    summ=2
    N=int(input())
    while n3<N:
        n3=n1+n2
        if n3>=N:
            continue
        n1=n2
        n2=n3
        if n3%2==0:
            summ+=n3
    print summ