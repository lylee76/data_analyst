#update calculator program using exception handeling
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    condition= input("Enter:\n 1 for Addition\n 2 for Subtration\n 3 for Multiplication\n 4 for Division\n")

    match condition:
        case "1":
            print(num1 + num2)
    
        case "2":
            print(num1 - num2)
    
        case "3":
            print(num1 * num2)
    
        case "4":
            print(num1 / num2)
    
        case _:
            print("Invalid")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("num2 cannot be zero.")  