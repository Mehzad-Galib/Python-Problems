L1 = ['A', 'B', 'C', 'D', 'E', 'F'];

L2 = ['G', 'H', 'I', 'J', 'K', 'L'];

result = []

for x in L1:
    for y in L2:
        result.append(x+y)
        
print("L1:",L1)
print("L2:",L2)
print('After combining L1 and L2:',result)

result.append('xyz')

print('result after appending xyz is:', result)
