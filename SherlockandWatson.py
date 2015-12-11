#https://www.hackerrank.com/challenges/sherlock-and-watson/submissions/code/10601550
# Enter your code here. Read input from STDIN. Print output to STDOUT
N,k,Q=[int(x) for x in raw_input().split()]
A = [int(x) for x in raw_input().split()]
k=k%N
B=A[-k:]+A[0:N-k]
for i in range(Q):
    print B[input()]


