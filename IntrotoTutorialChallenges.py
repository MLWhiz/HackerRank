#https://www.hackerrank.com/challenges/tutorial-intro/submissions/code/10588558
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
num= input()
n=input()    
tlist=[int(x) for x in raw_input().split(" ")]

for i,elem in enumerate(tlist):
    if elem ==num:
        print i
        break
