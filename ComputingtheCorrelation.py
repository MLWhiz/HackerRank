#https://www.hackerrank.com/challenges/computing-the-correlation/submissions/code/10573350
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
def svar(X):
    n = len(X)
    if n <= 1:
       raise ValueError, "sd(): n must be greater than 1"
    xbar = float(sum(X)) /n
    return (sum([(x-xbar)**2 for x in X])/(n-1))
 
def ssd(X):
    return sqrt(svar(X))

def pearsonr(X, Y, code = 0):
    """
    Computes pearson's correlation coefficient.
    code
       0 - using deviations from means.
       1 - common formula.
    """
    n = len(X)
    sx = ssd(X)
    sy = ssd(Y)
    xbar = float(sum(X)) / n
    ybar = float(sum(Y)) / n
    if code == 0:
       return sum([(x - xbar) * (y - ybar) for x, y in zip (X,Y)])/(sx * sy*(n-1.0))
    else:
       numer = sum([x*y for x,y in zip(X,Y)]) - n*(xbar * ybar)
       denom = sqrt((sum([x*x for x in X]) - n* xbar**2)*(sum([y*y for y in Y]) -n* ybar**2))
       return (numer /denom)
 
n =int(raw_input())
m=[]
p=[]
c=[]
for i in range(0,n):
    data=str(raw_input())
    M, P, C = data.split("\t")
    
    m.append(float(M))
    p.append(float(P))
    c.append(float(C))


print round(pearsonr(m,p),2)
print round(pearsonr(p,c),2)
print round(pearsonr(c,m),2)

