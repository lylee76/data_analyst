#loop
#loop are used to repeat the same block again and again
#There are two types of loop in python:
#1.for loop = when we know the start and stop condition
#2.while loop = When we don't know

#Syntax of for loop
#for variable(iterator) in iterable(group_data_type)
#block of code

#Iterator is a variable used to store current value of current iteration
#iteration is one complete round of loop
#iterable is a group data type

list1=[1,2,3,4,5]
dict ={
    "name":"Amylee",
    "age":"22"
}
#print(list1[0])
#print(list1[1])
#for i in list1:
    #print (i) //prints only keys
    #print(dict1[i])//prints only values

#for i in dict:
    #formatted string = combination of string and variable under single quotation
    #to use it we need to keep f at the start
    #print(f"key:{i} Value ={dict1[i]}")
    #print ("keys:", i)

#range method = is used to generate a sequence of numbers
#Syntax:
#range(start,stop,step)
#Start is inclusive= value is included
#stop is always exclusive = value is not included // means if u give (0 , 10) then prints 0 to 9 only
#for i in range(10):
    #print (i)

#While loop:
#the problem with while loop is it makes infinite loop if stopping condition is not given.
#syntax:
#while condition:
    #block of code
    #loop continues is the condition is true
    #if the condition false loop stops

#a=10 
#b=0
#while b<a:
    #print ("the condition is true")
    #b+=1

#break = when break keyword is encountered, the loop is terminated
#for i in range(6):
    #print (i)
    #if i==3 :
    #break
    #print("loop terminated")
    #print()

# Calculator using if-else, executed 5 times

for i in range(5):
    print("\nCalculation", i+1)

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operator (+ or -): ")

    if op == "+":
        result = a + b
        print("Result =", result)
    elif op == "-":
        result = a - b
        print("Result =", result)
    else:
        print("Invalid operator")

#pass helps in no error







