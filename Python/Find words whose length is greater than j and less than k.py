l = ['abc','de','fghij','k','lmn','opqrs','tuvw','xyz']
j,k = map(int,input("enter limits : ").split())
for i in l:
    if (len(i)>j) and (len(i)<k):
        print(i,end=" , ")