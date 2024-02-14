n = int(input("enter number : "))

s = str(n)

l = len(s)

sm = 0

for i in s:
    j = int(i)
    
    sm+=j**l
    
print(sm)

if sm==n:
    print('number is armstrong')
    
else:
    print("number is not armstrong")
