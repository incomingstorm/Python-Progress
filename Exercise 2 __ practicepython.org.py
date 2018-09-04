#Exercise 2 from practicepython.org: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

while True:
  print ("Options:")
  print ("Type 1 to check if a number is even or odd")
  print ("Type 2 to check if a number is a multiple of 4")
  print ("Type 3 to check if a number divides evenly into another number")
  print ("Type 'quit' to exit the program")
  user_input = input("Please enter your choice: ")

  if user_input == "1":
    num1 = int(input("Please enter a number to check if it's even or odd: "))
    if num1 % 2 == 0 :
      print ("The number "+str(num1)+" is even.")
    else :
      print ("The number "+str(num1)+" is odd")
  elif user_input == "2":
    num2 = int(input("Please enter a number to check it it's a multiple of 4 : "))
    if num2 % 4 == 0 : 
      print ("The number "+str(num2)+" is a multiple of 4.")
    else :
      print ("The number "+str(num2)+" is not a multiple of 4.")
  elif user_input == "3":
    num = float(input("Please enter the number you want to divide by: "))
    check = float(input("Please enter the other number: "))
    result = check % num
    print (result)
    if result == 0 or 0.0:
      print (str(check)+"%"+str(num)+" = ")
      print (result)
      print (str(num)+ " divides evenly into "+str(check))
    else:
      print (str(num)+" does not divide evenly into "+str(check))
  elif user_input == "quit":
    break 
   