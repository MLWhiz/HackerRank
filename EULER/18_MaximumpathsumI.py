#https://www.hackerrank.com/contests/projecteuler/challenges/euler018/submissions/code/4337757

def max_sum(data_list):
    if len(data_list)==1:
        return data_list[0][0]
    if len(data_list)==2:
        return data_list[0][0]+max(data_list[1])
    left_data_list = [x[1:] for x in data_list if len(x[1:])!=0]
    right_data_list = [x[:-1] for x in data_list if len(x[:-1])!=0]
    return data_list[0][0] + max(max_sum(left_data_list),max_sum(right_data_list))

cases=int(raw_input())
for i in range(cases):
    num_lines = int(raw_input())
    datalist=[]
    for i in range(num_lines):
        lin = [int(x) for x in raw_input().split(" ")]
        datalist.append(lin)
    print max_sum(datalist)