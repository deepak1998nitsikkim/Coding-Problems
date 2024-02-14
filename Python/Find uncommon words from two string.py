s1 = input("enter first string : ")
s2 = input("enter second string : ")


l1 = list()
l2 = list()

for i in s1.split(" "):
    l1.append(i)
    
for i in s2.split(" "):
    l2.append(i)
    
# print("string1 list : ",l1)
# print("string2 list",l2)

l3 = list()

for i in l1:
    if i not in l2:
        l3.append(i)

for i in l2:
    if i not in l1:
        l3.append(i)
        
print("Final list : ",l3)