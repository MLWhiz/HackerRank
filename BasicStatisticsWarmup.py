#https://www.hackerrank.com/challenges/stat-warmup/submissions/code/10578255
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
num=int(raw_input())
ints =[int(x) for x in raw_input().split(" ")]
import numpy as np
print np.mean(ints)
print np.median(ints)
from collections import defaultdict
d=defaultdict(int)
for int in ints:
    d[int]+=1
value=0
key=100000000000
for k,v in d.iteritems():
    if value<v:
        value=v
        key=k
    elif value==v:
        if key>k:
            key=k
print key
print round(np.std(ints),1)

import numpy as np
import scipy as sp
import scipy.stats
import math
def mean_confidence_interval(data, confidence=0.95):
    a = np.array(data)
    n = len(a)
    m, se = np.mean(a), np.std(a)/math.sqrt(num)
    h = se * 1.96
    return m-h, m+h

l,h=mean_confidence_interval(ints)
print round(l,1),round(h,1)