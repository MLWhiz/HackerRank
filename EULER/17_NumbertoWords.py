#https://www.hackerrank.com/contests/projecteuler/challenges/euler017/submissions/code/4336365
dict_data = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 
             9:"Nine", 10:"Ten",11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 
             17:"Seventeen", 18:"Eighteen", 19:"Nineteen",20: "Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty",
             70:"Seventy", 80:"Eighty", 90:"Ninety" ,100:"Hundred",1000: "Thousand", 1000000:"Million", 1000000000:"Billion", 1000000000000:"Trillion"}


def handle_hundreds(N):
    n = list(str(N))
    stri = ""
    if len(n)>=3:
        ind=len(n)-3+1
        num = int("".join(n[0:ind]))
        stri+=dict_data[num] + " Hundred"
        n=n[ind:]

    if len(n)>=2:
        ind=len(n)-2+1
        num = int("".join(n[0:ind]))*10
        if num==0:
            n=n[ind:]
        elif num!=10:
            stri+=" "+dict_data[num]
            n=n[ind:]
        else:
            num = int("".join(n[0:ind+1]))
            stri+=" "+dict_data[num]
            n=n[ind+1:]
    if len(n)==1:
        num = int(n[0])
        if num!=0:
            stri+=" "+dict_data[num]
    return stri.strip()

def answer(N):
    n = list(str(N))
    strd = ""
    if len(n)>=13:
        ind=len(n)-13+1
        num = int("".join(n[0:ind]))
        strd+=handle_hundreds(num)+ " Trillion"
        n=n[ind:]
    if len(n)>=10:
        ind=len(n)-10+1
        num = int("".join(n[0:ind]))
        if num!=0:
            strd+=handle_hundreds(num)+ " Billion"
        n=n[ind:]
    if len(n)>=7:
        ind=len(n)-7+1
        num = int("".join(n[0:ind]))
        if num!=0:
            strd+=" "+handle_hundreds(num)+ " Million"
        n=n[ind:]
    if len(n)>=4:
        ind=len(n)-4+1
        num = int("".join(n[0:ind]))
        if num!=0:
            strd+=" "+handle_hundreds(num)+ " Thousand"
        n=n[ind:]
    num = int("".join(n))
    strd+= " "+handle_hundreds(num)
    return strd


num_cases = int(raw_input())
for i in range(0,num_cases):
    x = int(raw_input())
    print answer(x).strip()