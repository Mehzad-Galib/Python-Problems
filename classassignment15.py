pre_L1 = []

print("Enter items for L1 below")

for i in range(0,5):
    pre_L1.append(int(input()))

L1 = []

for y in pre_L1:
    if y not in L1:
        L1.append(y)
      
L2 = []
for z in range(1,11):   
     if z not in L1:
         L2.append(z)
        
print('L1 is',L1)
print("L2 is",L2)

sorted_L1 = sorted(L1)
sorted_L2 = sorted(L2)


print('Sorted L1 is', sorted_L1)
print('Sorted L2 is', sorted_L2)

sorted_L1.reverse()

sorted_L2.reverse()

print('Reversed sorted L1 is', sorted_L1)
print('Reversed sorted L2 is', sorted_L2)

L3 = L1 + L2;

sorted_L3 = sorted(L3)

print('L1 and L2 Merged sorted list is', sorted_L3)

print('L1 and L2 Merge sorted and reversed list is', sorted_L3)