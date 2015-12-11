#https://www.hackerrank.com/contests/projecteuler/challenges/euler021/submissions/code/4337953\
def sum_factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return sum(result)-n

am_nums = set()
for i in range(0,10**5):
    if i not in am_nums:
        sf = sum_factors(i)
        d_sf = sum_factors(sf)
        if i==d_sf and sf!=d_sf:
            am_nums.add(i)
            am_nums.add(sf)

cases=int(raw_input())
for i in range(cases):
    num = int(raw_input())
    print sum([x for x in am_nums if x<=num])