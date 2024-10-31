number = input("Enter a number: ")

try:
    number = int(number)
    
    if number % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")
except ValueError:
    print("Please enter a valid integer.")
