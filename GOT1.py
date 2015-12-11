string = raw_input()
distalph=list(set(list(string)))
dict1={}
for char in distalph:
    cnt=0
    cnt=list(string).count(char)
    dict1[char]=cnt
odds=0
evens=0
for key in dict1:
    if dict1[key]%2==0:
        evens=evens+1
    else:
        odds=odds+1

if odds>1:
    found = False
else:
    found = True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

if not found:
    print("NO")
else:
    print("YES")