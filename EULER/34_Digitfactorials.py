#https://www.hackerrank.com/contests/projecteuler/challenges/euler034/submissions/code/1993629
def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
    
def check_curious(num):
    ls = list(str(num))
    ls = [int(x) for x in ls]
    ls1=[fact(x) for x in ls]
    #print ls1
    b=0
    for elem in ls1:
        b = b+elem
    #print b
    if b%num==0:
        return num
    else:
        return 0


num=input()
sum=0
for i in range(10,num):
    sum=sum+check_curious(i)
print sum
