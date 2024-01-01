#Author_Swarup:
import random

num = random.randrange(1,10)
num1 = int(input("Please guess a number from 1 to 10 : "))

while num != num1:
    if num < num1:
        print("Too Low")
        num1 = int(input("Please guess a number from 1 to 10 : "))
    elif num > num1:
        print("Too High")
        num1 = int(input("Please guess a number from 1 to 10 : "))
    else:
        break
print("You guessed it right !!")
