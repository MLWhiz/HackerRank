#https://www.hackerrank.com/challenges/the-best-aptitude-test/submissions/code/10577946
# Enter your code here. Read input from STDIN. Print output to STDOUT
from scipy.stats.stats import pearsonr

testcases=int(raw_input())
for i in range(0,testcases):
    #for every testcase
    num_stud=int(raw_input())
    scores=[float(x) for x in raw_input().split(" ")]
    #print scores
    pc=0
    for j in range(1,6):
        testcase = [float(x) for x in raw_input().split(" ")]
        #print testcase
        if pc<abs(pearsonr(testcase,scores)[0]):
            pc = abs(pearsonr(testcase,scores)[0])
            needed_i=j
    print needed_i