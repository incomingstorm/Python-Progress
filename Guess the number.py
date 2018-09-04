import random
player_name = input("Welcome to 'Guess the number'! What is your name?")
print ("Hello "+player_name+" ! I am thinking of a Number between 1 and 10.")
number_to_guess = random.randint(1,10)

while True:
  number_to_guess = random.randint(1,10)
  while True: #guesses_takes < 6:
    player_guess = int(input("Type in your guess: "))
        #guesses_taken = guesses_taken - 1
    if number_to_guess < player_guess :
      print ("Too high!")
    elif number_to_guess > player_guess :
      print ("Too low!")
    elif number_to_guess == player_guess :
      break
  print ("You guessed the number! ")
  start_again = input("Do you want to play again? (y/n)")
  if start_again == "n":
    break