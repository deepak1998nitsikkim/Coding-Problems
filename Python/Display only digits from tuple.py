t = (1,'a',3,'b','e',30.8,50,7.5,9,'ghi','ab','python')

for i in t:
    match i:
        case int():
            print(i)
            
        case float():
            print(i)