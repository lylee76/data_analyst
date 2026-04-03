#procedural programming - learnt till now
#Functional programming - The benefit of functional programming is it allows
#us to write reusable codes
#After defining the function, we must call it too

#Syntax:
#def function_name(paramenters)
    #block of code
    # return statement (optional)

#to call a function
#function_name(arguments)

#arguments are the values pass to the function
#paramenters are the variables that receives arguments

# def calculator(num1,num2,operator):
#     if operator == "+":
#         result= num1 + num2
#         print(f"The sum is :{result}")
#     elif operator == "-":
#         result = num1 - num2
#         print(f"The difference is: {result}")
#     elif operator == "*":
#         result = num1 * num2
#         print (f" The product is: {result}")
#     elif operator =="/":
#         if num2 != 0:
#             result = num1 / num2
#             print (f" The division is: {result}")
#         else:
#             print("Error. Division by zero is not allowed.")
#     elif operator == "%":
#         if num2 != 0:
#             result = num1 / num2
#             print (f" The modulus is: {result}")
#         else:
#             print("Error. Division by zero is not allowed.")
#     else:
#         print("Invalid operator. Enter a valid one.")
    

# choice = input("Enter operator (+,-,*,/,%):")
# operator = ["+", "-","*","/","%"]
# if choice in operator:
#     num1=int(input("Enter first number:"))
#     num2= int(input("Enter second number:"))
#     calculator(num1,num2,choice)
# else:
#     print("Invalid operator. Please enter the valid one.")

#built-in function: the fuctions are are pre-defined .
# e.g : input(), int(), print()

#user-defined function: the functions that are defined by users 
#eg: calculator()

#returnable function: Those functions that return value after execution
# non-returnable function: Those functions that does not return value

def sum(num1, num2):
    result = num1 + num2
    # return result
    print(f"The sum of {num1} and {num2} is: {result}")
    
# A function returns a value to where it is being called
    
# If a function returns some value,

# result123 = sum(5,10)
# print(result123)

# print(f"The result is {sum(5,10)}")

# print(sum(5,10))
sum(5,10)


