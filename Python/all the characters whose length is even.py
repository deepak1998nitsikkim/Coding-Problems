l = ['a','b','c','a','c','d','e','a','b','d','c','e']

el = {}

for i in l:
    if i in el:
        el[i]+=1
    
    else:
        el[i]=1

print("Characters with their count : ",el)

for i in el:
    if el[i]%2==0:
        print(i," : ",el[i],end= " , ")