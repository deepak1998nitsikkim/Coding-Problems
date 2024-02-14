s = input("enter string : ")
b = "01"

f=1

for i in s:
    if i not in b:
        f=0
        print('string is not binary')
        break
if f==1:
    print('string is binary')