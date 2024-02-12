mail = input("enter your mail here : ")

count_atrate = mail.count("@")

if count_atrate==1:
    
    atrate_index = mail.index("@")
    
    if len(mail[:atrate_index])>0:
        if len(mail[atrate_index+1:])>3:
            
            if mail[atrate_index+1:].count(".")==1:
            
                print("Your mail Id : ",mail)
                print("Your Username : ",mail[:atrate_index])
                print("Your Domain : ",mail[atrate_index+1:])
            
            else:
                print('Invalid Mail')
            
        else:
            print('Invalid Mail')
    else:
        print('Invalid Mail')

else:
    print('Invalid Mail')