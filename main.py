import random

number_of_dice = int(input("How many dice do you want to roll?\n"))
n = 0

for i in range(1, number_of_dice+1):
    number = random.randint(1, 6)
    n += number

print("The sum of all the numbers on the dice is " + str(n))
