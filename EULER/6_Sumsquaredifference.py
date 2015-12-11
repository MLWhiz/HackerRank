#https://www.hackerrank.com/contests/projecteuler/challenges/euler006/submissions/code/2542676
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    n=int(input())
    print (n*(n+1)/2)**2 - (n*(n+1)*(2*n+1))/6