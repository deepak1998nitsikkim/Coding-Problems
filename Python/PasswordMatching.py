import random,string

ac = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
print(ac)

gp = ""
sp = input("Enter System Password : ")

c=0

while True:
    for i in range(len(sp)):
        r = random.choice(ac)
        gp+=r
        
    print("\nPassword is not matching : ",gp)
    c+=1
    
    if gp==sp:
        print('\nYour Password is correct')
        print("\nSystem Password : ",sp," : \tGuess Password : ",gp)
        print('\nTotal Trials : ',c)
        break
    
    else:
        gp=""
    
