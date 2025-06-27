#find particular value particular index

l = [1,4,3,1,7,1,5,8,1,3,2,3,4,5]
l2=[]
v = int(input('enter value : '))
for i,j in enumerate(l):
    if j==v:
        l2.append(i)
        print(i)
x = int(input('find nth index : '))
for i in range(len(l2)):
    if x>len(l2):
        print('not possible')
        break
    elif x==(i+1):
        print(l2[i])
        
