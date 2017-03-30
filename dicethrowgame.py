#! /usr/bin/python3

# Dice rolling game.

import random

print("Dicerolling game.\nPress r to roll and q to quit")

# mainloop

while True:
    valid_answers = ["r", "q"]
    answer = str(input("Please enter: "))
    if answer not in valid_answers:
        continue
    elif answer == valid_answers[0]:
        print(str(random.randint(1, 6)))
    else:
        break
