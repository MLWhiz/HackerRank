input= raw_input()
c=input.split(" ")
num_elems = int(c[0])
test_cases = int(c[1])
sum=0
for i in range(0,test_cases):
    inp=raw_input()
    c=inp.split(" ")
    a = int(c[0])
    b = int(c[1])
    k = int(c[2])
    sum=sum+k*(b-a+1)
    #ls=[0]*(a-1)+[k]*(b-a+1)+[0]*(num_elems-b)
    #print sum
print sum/num_elems
    