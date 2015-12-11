#https://www.hackerrank.com/contests/projecteuler/challenges/euler010/submissions/code/2542945
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=1000000
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
#print(len(fin_arr))

#precompute
'''
fin_sums=fin_arr
for i in range(1,len(fin_arr)):
    fin_sums[i]=fin_sums[i]+fin_sums[i-1]
print "done"
'''
inp_a=[]
for tc in range(int(input())):
    a=input()
    inp_a.append(a)

inp_a_sort=list(inp_a)
inp_a_sort.sort()
#print inp_a
#print inp_a_sort
sum=0
sum_array={}
for a in inp_a_sort:
    for i,elem in enumerate(fin_arr):
        if elem<=a:
            sum += elem
        else:
            fin_arr=fin_arr[i:]
            break
    sum_array[a]=sum

for elem in inp_a:
    print sum_array[elem]
    

