def cel_to_far(c):
    return 1.8*c+32

def far_to_cel(f):
    return (f-32)/1.8

print("Enter Celcius Value")

cel = int(input())

print("The farenheight value is:", cel_to_far(cel))

print("Enter Farenheight Value")

far = int(input())

print("The farenheight value is:", far_to_cel(far))