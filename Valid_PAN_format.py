#https://www.hackerrank.com/challenges/valid-pan-format/submissions/code/10523482
# Enter your code here. Read input from STDIN. Print output to STDOUT
#<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>
import re
cases =int(raw_input())
for i in range(0,cases):
    string = raw_input()
    match=re.search(r'[A-Z]{5}[0-9]{4}[A-Z]',string)
    if match:
        print "YES"
    else:
        print "NO"
        