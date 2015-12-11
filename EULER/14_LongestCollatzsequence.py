#https://www.hackerrank.com/contests/projecteuler/challenges/euler014/submissions/code/4336022
dict_num_len = [0]*5000001
def create_coll(N):
    if N<=5000000 and dict_num_len[N]!=0:
        return dict_num_len[N]
    else:
        if N==1 or N==0:
            return 1
        elif N%2==0:
            length = 1 + create_coll(N/2)
            if N<=5000000:
                dict_num_len[N]=length
        else:
            length = 1 + create_coll(3*N+1)
            if N<=5000000:
                dict_num_len[N]=length
        return length

num_cases = int(raw_input())
cases_list = []
for i in range(0,num_cases):
	num = int(raw_input())
	cases_list.append(num)

max_num = max(cases_list)

ans_list = [0]*(max_num+1)
max_i = None
max_length = 0
for i in range(1,max_num+1):
	sq_length = create_coll(i)
	if sq_length>=max_length:
		max_i = i
		max_length = sq_length
	ans_list[i] = max_i

for x in cases_list:
    print ans_list[x]