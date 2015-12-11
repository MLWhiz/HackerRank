#https://www.hackerrank.com/challenges/split-number/submissions/code/10523544
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
#<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>
'''2
1 877 2638277
91-011-23413627
'''
import re
cases =int(raw_input())
for i in range(0,cases):
    string = raw_input()
    match=re.search(r'([0-9]{1,3})[- ]([0-9]{1,3})[- ]([0-9]{4,10})',string)
    if match:
        print "CountryCode="+match.group(1)+",LocalAreaCode="+match.group(2)+",Number="+match.group(3)

        