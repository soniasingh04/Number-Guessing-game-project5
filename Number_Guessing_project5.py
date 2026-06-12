import random
Computer_number = random.randint(1,101)
userInput=int(input("Enter your number: "))
if userInput>Computer_number:
    print("Computer number is ", Computer_number)
    print("Your number is greater than computer number")
elif userInput<Computer_number:
    print("Computer number is ", Computer_number)
    print("Your number is smaller than computer number")
else:
    print("Computer number is ", Computer_number)
    print("Congratulations! You guessed the number correctly.")        