n = int(input("enter range : "))

i=0
n1=0
n2=1

while i<n:
    
    print(n1,end=" ")
    
    n3=n1+n2
    n1=n2
    n2=n3
    i+=1
