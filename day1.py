#comment
#comments always with # in python
#Python does not support multi-line comments
#For multi-line comments we can use """

#variables are used to store data by users
#variables in python doesnot require data type declaration
# variable_name = value(data_type)
#name = "John" #string
#age = 30 #integer

#Naming conventions
#There are 4 types of naming conventions
#1. Camel Case: firstName, lastName(first letter of the first word is lowercase and the first letter of the next word is uppercase)
#2. Pascal Case: FirstName, LastName(first letter of each word is uppercase)
#3. Snake Case: first_name, last_name(all letters are lowercase and words are separated by underscores)
#4. Kebab Case: first-name, last-name (not used in python)


#first program in python
print("hello world")

#WAP to print your name
print("My name is Amylee")

#input() function is used to take input from the user
#It always returns a string, so we need to convert it to the desired data type if needed using type casting
num1 = input("Enter first number:")
num2 = input ("Enter second number:")
print(num1 + num2)
#The above code will concatenate the two numbers as they are treated as strings
#To perform addition we need to convert them to integers

#typecasting 
num1 = int(input("Enter first number:"))
num2 = int(input ("Enter second number:"))
print(num1 + num2)

#Make a calculator that takes user input and performs basic arithmetic operations
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)