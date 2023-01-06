# defining a  class
class Person:
    def __init__(self, name, age):
        self.name =name
        self.age=age

# objects
per1=Person("Cyrus", 22)



# calling
print ("The name is :", per1.name)
print("The age is: ", per1.age)

# userinput
a=input("New user name: ")
b=int(input("Enter age: "))

# object2
per2=Person(a,b)


print ("The name is :", per2.name)
print ("The name is :", per2.age)