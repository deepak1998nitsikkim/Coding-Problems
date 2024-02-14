l = [2,1,6,5,7,9]
k = int(input("enter divider element : "))

for i in l:
    if i%k==0:
        print("First occure element : ",i)
        break
