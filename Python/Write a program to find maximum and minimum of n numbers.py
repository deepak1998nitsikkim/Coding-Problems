n = int(input("enter range : "))

l = list()

for i in range(n):
    x = int(input("enter number : "))
    l.append(x)
    
mx = l[0]
mn = l[0]

for i in l:
    if mx<=i:
        mx=i
        
    if mn>=i:
        mn=i
        
print("Maximum Value : ",mx)
print("Minimum Value : ",mn)