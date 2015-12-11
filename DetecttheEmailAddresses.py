#https://www.hackerrank.com/challenges/detect-the-email-addresses/submissions/code/10524113
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
#<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>
import re
cases =int(raw_input())
links=[]
for i in range(0,cases):
    string = raw_input()
    try:
        match=re.findall(r'([\w0-9-._]+@[\w0-9-.]+[\w0-9]{2,3})',string)
        for elem in match:
            #print elem
            links.append(elem.strip())
    except:
        pass
    
links=list(set(links))
linked =links
linked.sort()
print ";".join(linked)