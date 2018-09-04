#Exercise 1 from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html


from datetime import datetime
currentYear = datetime.now().year
currentMonth = datetime.now().month
print (currentYear)
print (currentMonth)

name_user = str(input("What is your name?"))
age_user = int(input("Hello "+name_user+", how old are you?"))
add_100 = age_user + 100

birthyear_user = int(input("What year were you born, "+name_user+" ?"))

while currentYear - birthyear_user != age_user: 
  
  if currentYear - birthyear_user != age_user :
    print ("That can't be right if you are actually "+str(age_user)+" Years old. Please type in the correct year.")
    birthyear_user = int(input("What year were you born, "+name_user+" ?"))
  else :
    break
turn_100 = birthyear_user + 100
print ("In the Year "+str(turn_100)+" you will turn 100, "+name_user+".")


age_message = "And in 100 Years you will be "+ str(add_100) +" Years old!"+'\n'
print (age_message)
random_number = int(input("Please enter a random number: "))
print (age_message * random_number)
