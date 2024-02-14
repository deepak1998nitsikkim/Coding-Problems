l = [5,2,1,7,6,8,9,20,16,18,29,50,27]

l1 = sorted(l)
l2 = l1[::-1]

n = int(input("enter result for nth : "))

print(l)
print(l1)
print(l2)

print(l1[n-1])
print(l2[n-1])