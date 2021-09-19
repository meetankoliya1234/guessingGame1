import random
number = (random.random())
chances = 0
guess = int(input("guess a number (between 1 to 9):"))
while chances >= 5:
    if guess == number:
       print("Congrtulations You Won!!!")
       break
    if not chances >= 5:
        print("You Lose!!! This Number is", number)