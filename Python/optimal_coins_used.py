coins =0
l = []
l1=[]
m=0
a = int(input('enter your amount : '))
n = int(input('How many diffferent types of coins we want to use : '))

for i in range(n):
    x= int(input('enter coin price : '))
    l.append(x)

while a>0:
    for i in l:
        if i<=a:
            # print(i,end=' ')
            l1.append(i)
            
    # print('\n')
    
    m=max(l1)
    print(m)
    
    l1=[]
    
    a=a-m
    
    coins+=1
print('total coins used : ',coins)

