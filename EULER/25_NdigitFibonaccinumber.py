#https://www.hackerrank.com/contests/projecteuler/challenges/euler025/submissions/code/4340189
array = [0]*5001
i=0
num1 = 0
num2 = 1
num3 = 1
len_covered = 1
while len_covered<5001:
    num1 = num2
    num2 = num3
    num3 = num1+num2
    if len(str(num3))==len_covered:
        array[len_covered] = i+3 
        len_covered+=1
    i+=1
array[1]=0
cases=int(raw_input())
for i in range(cases):
    num = int(raw_input())
    print array[num]