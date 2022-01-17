import random

count = 0

while 1:
    randomNum = random.randint(1,10)
    guess = int(input("Enter an integer from 1 to 10: "))
    
    if randomNum == guess:
        print('Your guess is correct!')
        print('random number was',randomNum)
        print('you guessed ',guess)
        count += 1
        break
    else: 
        count += 1
        print('random number was',randomNum)
        print('you guessed ',guess)
        print('guess again')
        continue

print('Total Attempt:', count)