#https://www.hackerrank.com/challenges/connecting-towns/submissions/code/10588544
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
ts= input()
for i in range(0,ts):
    n=input()
    tlist=[int(x) for x in raw_input().split(" ")]
    num=1
    for elem in tlist:
        num=num*elem
    print num%1234567