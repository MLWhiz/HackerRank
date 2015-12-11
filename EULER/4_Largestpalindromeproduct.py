#https://www.hackerrank.com/contests/projecteuler/challenges/euler004/submissions/code/2542612
# Enter your code here. Read input from STDIN. Print output to STDOUT
ls=[]
for i in range(100,1000):
    for j in range(100,1000):
        n=str(i*j)
        if n==n[::-1] and len(n)==6:
            ls.append(int(n))

for i in range(int(input())):
    N = int(input())
    max_elem=0
    for elem in ls:
        if elem<N and elem>max_elem:
            max_elem=elem
    print max_elem
    