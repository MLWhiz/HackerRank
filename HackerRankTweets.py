#https://www.hackerrank.com/challenges/hackerrank-tweets/submissions/code/10523518
# Enter your code here. Read input from STDIN. Print output to STDOUT
#<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>
import re
cases =int(raw_input())
cnt=0
for i in range(0,cases):
    string = raw_input()
    match=re.search(r'hackerrank',string,re.IGNORECASE)
    if match:
        cnt+=1
print cnt