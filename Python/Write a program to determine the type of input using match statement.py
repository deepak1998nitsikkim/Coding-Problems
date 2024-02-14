# Program to determine the type of input using match statement
data = eval(input("enter data : "))

match data:
    
    case int():
        print('Integer Type')
    
    case float():
        print('Float Type')
    
    case str():
        print('String Type')
    
    case list():
        print('List Type')
    
    case set():
        print('Set Type')
    
    case tuple():
        print('Tuple Type')
    
    case dict():
        print('Dictionary Type')
