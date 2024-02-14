l = ['a','b','c','a','c','d','e']

el = {}
nl = list()

for i in l:
    if i in el:
        el[i]+=1
        
    else:
        el[i]=1
        
print("Characters with counts : ",el)

for i in el:
    if el[i]==1:
      nl.append(i)

print("Unique elements : ",nl)

# for i in el:
#     if el[i]!=1:
#       nl.append(i)

# print("Duplicate elements : ",nl)