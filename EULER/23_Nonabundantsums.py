#https://www.hackerrank.com/contests/projecteuler/challenges/euler023/submissions/code/4338040
def sum_factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return sum(result)-n

predefined = 28123
AN = []
for i in range(12,predefined+1):
    if sum_factors(i)>i:
        AN.append(i)

def check_yes_no(n,AN):
    decision ="NO"
    if n>=predefined:
        decision="YES"
    else:
        for elem in AN:
            if elem >=n:
                break
            if n-elem in AN:
                decision = "YES"
                break
    print decision

cases=int(raw_input())
for i in range(cases):
    num = int(raw_input())
    check_yes_no(num,AN)
