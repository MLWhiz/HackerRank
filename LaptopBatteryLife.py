#https://www.hackerrank.com/challenges/battery/submissions/code/10573050
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
data = float(sys.stdin.readline())

if data >= 4.00:
    print 8.00
else:
    print round(2*data, 2)
