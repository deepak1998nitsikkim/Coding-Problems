currency =0
l = [2000,1000,500,200,100,50,20,10,5,2,1]
l1=[]
l2=[]
m=0
a = int(input('enter your amount : '))
while a>0:
    for i in l:
        if i<=a:
            # print(i,end=' ')
            l1.append(i)
            
    # print('\n')
    
    m=max(l1)
    l2.append(m)
    print(m)
    
    l1=[]
    
    a=a-m
    
    currency+=1
print('total notes/coins used : ',currency)
print('total unique notes/coins used : ',len(set(l2)))
