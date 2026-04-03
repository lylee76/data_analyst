class Student:
    college_name = "Mindrisers Institute"
    
    def __init__(self, name, gender, age, address):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address
        
        
std1 = Student("Amylee", "female",22, "sitapaila")
print(std1.college_name)
print(std1.name)
print(std1.age)
print(std1.address)
print(std1.age)
print()
print()
std2 = Student("Amy ","Female",20,"sita")
print(std2.college_name)
print(std2.name)
print(std2.age)
print(std2.gender)
print(std2.address)
print()
print()
std3 = Student("Arpana","Female",20,"pokhara")
print(std3.college_name)
print(std3.name)
print(std3.age)
print(std3.gender)
print(std3.address)
std4 = Student("Sonu ","Female",21,"siliguri")
print(std4.college_name)
print(std4.name)
print(std4.age)
print(std4.gender)
print(std4.address)
print()
print()
std5 = Student("Arpan","male",26,"penure")
print(std5.college_name)
print(std5.name)
print(std5.age)
print(std5.gender)
print(std5.address)

