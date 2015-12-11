#https://www.hackerrank.com/contests/projecteuler/challenges/euler024/submissions/code/4339106
new_fact = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800,87178291200]
fact_list = [0, 0, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800,87178291200]
def get_nth_perm(alpha,n):
    lower,upper,lower_ind,upper_ind = 0,0,0,0
    for i in range(len(new_fact)-1):
        if n>new_fact[i] and n<=new_fact[i+1]:
            lower = new_fact[i]
            upper = new_fact[i+1]
            lower_ind = i
            upper_ind = i+1
    #print lower,upper,lower_ind,upper_ind
    if len(alpha)-upper_ind-1>0:
        starting_part = alpha[0:len(alpha)-upper_ind-1]
        end_part = alpha[len(alpha)-upper_ind-1:]
    else:
        starting_part=''
        end_part=alpha
    #print "Start:"+starting_part
    return starting_part + get_end(end_part,n)
    

def get_end(alpha,n):
    if n==0:
        return alpha
    if n==1 and len(alpha)==2:
        return alpha[1]+alpha[0]
    elif n==1 and len(alpha)==1:
        return alpha
    num=fact_list[len(alpha)-1]
    ind = n/num
    new_alpha = alpha.replace(alpha[ind],'')
    new_n = n%num
    return alpha[ind]+get_end(new_alpha,new_n)

alpha = "abcdefghijklm"
num_cases = int(raw_input())
for i in range(num_cases):
    num = int(raw_input())
    print get_nth_perm(alpha,num-1)
