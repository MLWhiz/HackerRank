#https://www.hackerrank.com/challenges/find-hackerrank/submissions/code/10523248
# Enter your code here. Read input from STDIN. Print output to STDOUT

cases=int(raw_input())
for i in range(0,cases):
    string = raw_input()
    if string[:10]== 'hackerrank' and string[-10:]== 'hackerrank':
        print 0
    elif string[:10]== 'hackerrank':
        print 1
    elif string[-10:]== 'hackerrank':
        print 2
    else:
        print -1