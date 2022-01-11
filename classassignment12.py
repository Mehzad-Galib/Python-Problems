num = int(input("Please input your number: "))

if num >= 80:
    print('A+')

elif 79 >= num >= 75:
    print("A")

elif 74 >= num >= 70:
    print("A-")

elif 69 >= num >= 65:
    print("B+")

elif 64 >= num >= 60:
    print("B")

elif 59 >= num >= 56:
    print("B-")

elif 55 >= num >= 50:
    print("C+")

elif 49 >= num >= 45:
    print("C")

elif 44 >= num >= 40:
    print("D")

else:
    print("F")
