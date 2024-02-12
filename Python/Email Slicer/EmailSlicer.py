email = input("enter your email here : ")

count_atrate = email.count("@")
atrate_index = email.index("@")

if count_atrate==1:
    if len(email[:atrate_index])>0:
        if len(email[atrate_index+1:])>3:
            print("Your Email Id : ",email)
            print("Your Username : ",email[:atrate_index])
            print("Your Domain : ",email[atrate_index+1:])
        
        else:
            print('Invalid Mail')
    else:
        print('Invalid Mail')

else:
    print('Invalid Mail')