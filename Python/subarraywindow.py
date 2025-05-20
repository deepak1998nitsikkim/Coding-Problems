#Maximum sum subarray of some window size

a = [2,5,6,4,8,7,3]
ws = int(input('enter window size : '))

for i in range(len(a)-ws+1):
    c=0
    for j in range(i,i+ws):
        c+=a[j]
    print(c)
