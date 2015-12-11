#https://www.hackerrank.com/challenges/power-of-large-numbers/submissions/code/10601856
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
for i in range(input()):
    a,b = [int(x) for x in raw_input().split(" ")]
    print pow(a,b,10**9+7)