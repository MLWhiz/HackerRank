#https://www.hackerrank.com/contests/projecteuler/challenges/euler016/submissions/code/4336172
# Enter your code here. Read input from STDIN. Print output to STDOUT

def power_digit_sum(N):
    a = 2**N
    return sum([int(x) for x in list(str(a))])

num_cases = int(raw_input())
for i in range(0,num_cases):
    N = int(raw_input())
    print power_digit_sum(N)