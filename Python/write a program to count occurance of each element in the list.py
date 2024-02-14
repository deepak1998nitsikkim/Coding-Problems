l = [2,1,2,1,4,3,6,8,9,6,6]

ec = {}

for i in l:
    if i in ec:
        ec[i]+=1
    else:
        ec[i]=1
print(ec)