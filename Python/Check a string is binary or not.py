s = input("enter string : ")

bs = "01"
f=0
for i in s:
    if i not in bs:
        f=1
        print("Not Binary")
        break
        
if f==0:
    print('Binary')