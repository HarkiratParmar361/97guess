import random
number = random.randint(1, 9)
chanceCount = 0
while (chanceCount < 5):
    introString = int(input("enter the number between 1-9: "))
    if (introString > number):
        print("Lower!!")
    elif (introString == number):
        print("WOW! Great Job Your Guess was Correct!!!")
    else :
        print("Higher!!")
    chanceCount = chanceCount + 1
if (chanceCount > 5):
    print("Game Over you Lose!")
