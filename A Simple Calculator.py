\\ A simple Calculator

while True:												\\ The user menu
    print ("Options:")
    print ("Enter 'add' to add two numbers")
    print ("Enter 'subtract' to subtract two numbers")
    print ("Enter 'multiply' to multiply two numbers")
    print ("Enter 'divide' to divide two numbers")
    print ("Enter 'quit' to exit the program")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        x = num1 + num2
        print (x)
    elif user_input == "subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        x = num1 - num2
        print (x)
    elif user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        x = num1 * num2
        print(x)
    elif user_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        x =  num1 / num2
        print(x)
		