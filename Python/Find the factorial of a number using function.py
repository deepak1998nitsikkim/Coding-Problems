def fact(n):
    p=1
    
    for i in range(1,n+1):
        p*=i
    
    print("Factorial of ",n," : ",p)

n = int(input("enter number : "))

fact(n)