s = input("enter string : ")
v = "aeiouAEIOU"

sn = ""
for i in s:
    if i in v:
        continue
    sn+=i
print(sn)