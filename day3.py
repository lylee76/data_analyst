#list data type
#List is a mutable data type which means its content can be changed.
#List is a group data type
#Anything can be stored in list like int,float,boolean,string or another list
#It is defined by using [] square brackets.

#list1 = [1,2.5,True, "Amylee",[3,4,5],7,"pakhrin"]
#print(list1)
#print(type(list1))
#list1.append("Tamang")
#print(list1)
#append is a method in list that is used to add new element at last index

#indexing and slicing in list

#print(list1[2])

#indexing nested list values
#another_list = list1[4]
#print(another_list[1])

#tuples
#tuples is a group data type that is immutable in nature
#tuples is wrapped in () small bracets
#tuples value cannot be changed hence it is used to store constant values

#tuple =(1,2,3,"WTF", False,("amylee",4,5),False,9,10)
#print(tuple)

#indexing and slicing is same as list
#print(tuple[-1])#prints last element

#set
#set is unordered and unindexed
#output can be in any order

#dictionary
#It is a group data type that is ordered, mutable and indexed
#It always comes in key:value pair
#It is enclosed in {}curly braces
dict = {
    "name":"Amylee",
    "age": 40,
    "address": "Sitapaila",
    "phone": 9810367014,
    "email": "pakhrinamylee@gmail.com"
}
#print(dict)
#print(dict.keys())
#print(dict.values())
#print(dict["email"])

#Login system with existing list of usernames
usernames = ["Amylee", "Arpana", "Sonu","piss"]

user =input("Enter your username:")

if user in usernames:
    print("Login Successful")
else:
    print("Login failed")

#Take username from user and append it to the list of username
user =input("Enter your username:")
usernames=[]
usernames.append(user)
print("Registration successful")
user_login =input("Enter your username:")
if user_login in usernames:
    print("Login success")
else:
    print("Login failed")


