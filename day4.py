#check the username is present in the list or not
username =["Amylee", "Arpana","Sonu","Shaily"]
user = input("Enter the username:")
if user in username:
    print("username is present")
else:
    print("username not present")

#Create a dictionary of usernames and passwords,extract all the usernames 
# from the dictionary and input username from the user and check if the 
# username is present in the extracted list of 	usernames
dict = {
    "Amylee" : "amylee123",
    "Sonu" : "Sonu123",
    "Ruby" : "Rubytupi123",
    "Arpana" : "Arpana6767"
}
print(dict.keys())

username =input("Enter the username:")
if username in dict:
    print("Username is present")
else:
    print("Username not present")

#Calculator program using if...else
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
condition = int(input("Enter: \n 1 for Addition\n 2 for Subtraction\n 3 for Multiplication\n 4 for Division\n"))
if condition ==1:
    print(num1 + num2)
elif condition ==2:
    print (num1 - num2)
elif condition ==3:
    print (num1 * num2)
elif condition ==4:
    print (num1 / num2)
else:
    print("Invalid")

#find the greatest and smallest numbers among 3 numbers
num1 =int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if num1 > num2 and num1 > num3:
    print(num1, "is greatest")
elif num2 > num1 and num2 > num3:
    print(num2, "is greatest")
else:
    print(num3, "is greatest")

if num1 < num2 and num1 < num3:
    print(num1, "is smallest")
elif num2 < num1 and num2 < num3:
    print(num2, "is smallest")
else:
    print(num3, "is smallest")

#calculator using match 
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

#find greatest and smallest 

num1 = int(input("Enter first number:"))
num2 = int (input("Enter second number:"))
num3 = int( input("Enter third number:"))

match True:
    case _ if num1> num2 and num1>num3:
        print(num1, "is greatest")

    case _ if num2 > num1 and num2 > num3:
        print(num2, "is greatest")
    
    case _:
        print(num3, "is greatest")


