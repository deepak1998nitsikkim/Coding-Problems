l = list()

n = int(input("enter range : "))

n1=0
n2=1

for i in range(n):
    
    l.append(n1)
    
    n3=n1+n2
    n1=n2
    n2=n3
    
print(l)
print(l[3])