#https://www.hackerrank.com/contests/projecteuler/challenges/euler007/submissions/code/2542823
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=150000
A=[1]*n
i=2
while i<=math.sqrt(n):
    #print i 
    if A[i]==1:
        j=i**2
        while j<n:
            #print j
            A[j] = 0    
            j+=i
    i+=1

fin_arr=[]
for i,j in enumerate(A):
    if j==1:
        fin_arr.append(i)
fin_arr=fin_arr[2:]

 
for tc in range(int(input())):
    print fin_arr[int(input())-1]
    
    
    