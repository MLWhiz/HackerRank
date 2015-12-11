#https://www.hackerrank.com/contests/projecteuler/challenges/euler015/submissions/code/4336145
MM = 10**9+7
memorize = [[0 for i in range(502)] for j in range(502)]
def find_paths(M,N):
    if M==1 and N==1:
        return 2
    if M==0 or N==0:
        return 1
    if memorize[M][N]!=0:
        return memorize[M][N]
    memorize[M][N]=find_paths(M-1,N)+find_paths(M,N-1)
    return memorize[M][N]

num_cases = int(raw_input())
for i in range(0,num_cases):
    x = raw_input().split(" ")
    m = int(x[0])
    n = int(x[1])
    print find_paths(m,n)%MM