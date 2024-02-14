l = [4,3,2,0]

al = sorted(l)
dl = al[::-1]

if (l==al) or (l==dl):
    print("Monotonic")
    
else:
    print("Not Monotonic")