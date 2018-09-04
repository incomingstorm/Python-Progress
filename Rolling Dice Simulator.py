# Dice Rolling Simulator


import random
input("Press enter to roll the Dice.")
print (random.randint(1, 6))
while True:
    user_input = input("Would you like to roll again?")
    if user_input == "no":
        break
    elif user_input == "yes":
        print (random.randint(1, 6))
   