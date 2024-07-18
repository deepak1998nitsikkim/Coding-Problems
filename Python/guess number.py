import random

guess = random.randint(1,1000)

user = int(input("enter your number : "))

trial = 0

if user == guess:
    print('Your guess is absolutely correct\n')
    
else:
    while user!=guess:
        if user<guess:
            print('Your guess number is small')
            user = int(input("Please enter your number again: "))
            trial+=1
            
        else:
            print('Your guess number is big')
            user = int(input("Please enter your number again: "))
            trial+=1

print("\nTotal guesses = ",trial)
        

        
    