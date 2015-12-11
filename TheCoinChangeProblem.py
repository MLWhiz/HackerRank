#https://www.hackerrank.com/challenges/coin-change/submissions/code/2553771
# Enter your code here. Read input from STDIN. Print output to STDOUT
#0<=sum_needed<=250
coins = [int(x) for x in raw_input().split(",")]
sum_needed=input()
total_coins=len(coins)

def count_solution(coins,coin_num,sum):
    if sum==0:
        return 1
    elif sum<0:
        return 0
    elif coin_num<=0 and sum>=1:
        return 0

    return count_solution(coins,coin_num,sum-coins[coin_num-1])+count_solution(coins,coin_num-1,sum)


def count(S, m, n ):
    ls=[0 for x in range(n+1)]
    ls[0] = 1
    for i in range(0,m):
        for j in range(S[i],n+1):
            ls[j] += ls[j-S[i]]
    return ls[n]

            
    
print count(coins,total_coins,sum_needed)
