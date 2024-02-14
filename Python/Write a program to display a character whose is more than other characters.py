l = ['a','c','b','a','d','a','a','b','e','b','b','b']

print("List : ",l)
d = {}

for i in l:
    if i in d:
        d[i]+=1
        
    else:
        d[i]=1
        
# print("Dictionary : ",d)

kl = list()
vl = list()

for i in d:
    kl.append(i)
    vl.append(d[i])
    
# print("keys : ",kl)
# print("values : ",vl)

mx = vl[0]

for i in vl:
    if mx<i:
        mx=i
        
for i in d:
    if mx==d[i]:
        print(i," : ",d[i])