#https://www.hackerrank.com/challenges/detect-the-domain-name/submissions/code/10524043
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
#<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>
import re
cases =int(raw_input())
links=[]
for i in range(0,cases):
    string = raw_input()
    try:
        match=re.findall(r'http(s:|:)\/\/(www.|ww2.|)([0-9a-z.A-Z-]*\.\w{2,3})',string)
        for elem in match:
            #print elem
            links.append(elem[2].strip())
    except:
        pass
    
links=list(set(links))
linked =links
linked.sort()
print ";".join(linked)