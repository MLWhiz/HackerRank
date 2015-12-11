#https://www.hackerrank.com/contests/projecteuler/challenges/euler008/submissions/code/2542842
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    N,k = [int(x) for x in raw_input().split(" ")]
    n=list(raw_input())
    max_mul=0
    for i in range(0,N-k):
        mul=1
        for j in range(k):
            mul*=int(n[i+j])
    #print mul
        if mul>max_mul:
            max_mul=mul
    print max_mul
