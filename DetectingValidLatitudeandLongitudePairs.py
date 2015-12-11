#https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/submissions/code/10523702
'''
12
(75, 180)
(+90.0, -147.45)
(77.11112223331, 149.99999999)
(+90, +180)
(90, 180)
(-90.00000, -180.0000)
(75, 280)
(+190.0, -147.45)
(77.11112223331, 249.99999999)
(+90, +180.2)
(90., 180.)
(-090.00000, -180.0000)
'''
import re
cases =int(raw_input())
for i in range(0,cases):
    string = raw_input()
    match=re.search(r'^\((\+|-|)([1-9][0-9.]*), (\+|-|)([1-9][0-9.]*)\)$',string)
    if match:
        try:
            if float(match.group(2))<=90.0 and float(match.group(4))<=180.0 and match.group(4)[-1:]!="." and match.group(2)[-1:]!="." :
                print "Valid"
            else:
                print "Invalid"    
        except:
            print "Invalid"
    else:
        print "Invalid"