num1 = input()


dict1={}
for i in range(0,num1):
    stri= str(raw_input())
    stri1=list(set([a for a in stri]))
    for elem in stri1:
        if elem in dict1:
            dict1[elem]+=1
        else:
            dict1[elem]=1
num=0
for key in dict1:
    if dict1[key]==num1:
        num+=1
print num