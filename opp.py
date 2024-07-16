# # # The __str__() function controls what should be returned when the class object is represented as a string.
# # # If the __str__()function is not set, the string representation of an object without the __str__()function.
# # class Person:
# #     def __init__(self, name , age):
# #         self.n = name
# #         self.a = age
        
        
# # p1 = Person("Aminul" , 25)
# # print(p1.n ,p1.a)
# # print(p1.n)
# # The string representation of an object with the __str__()function
# # class Person:
# #     def __init__(self, name , age):
# #         self.name = name
# #         self.age = age
        
        
# #     def __str__(self):
# #         return f"My name is {self.name}. And i am {self.age} years old."
    
    
# # p1 = Person("Aminul" , 25)

# # print(p1)
# class Data:
#     def __init__(self, name , id, age , experience):
#         self.name = name
#         self.id = id
#         self.age=age
#         self.experience = experience
        
        
#     def __str__(self):
#         return f"My name is {self.name}.The counter info ID:{self.id}.I am {self.age} years old. And i am job experience with {self.experience} years almost."
    
    
# d1 = Data('Aminul Islam','231-134-032','24','7')

# print(d1)
# class Person:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
        
        
#     def myfunction(self):
#         print("Hello my name is " + self.name)
        
# p1 = Person("John" , 36)
# p1.myfunction()
# class Person:
#     def __inti__(mysillyobject, name , age):
#         mysillyobject.name = name
#         mysillyobject.age = age
        
        
#     def myfunc(abc):
#         print("Hello my name is " + abc.name)
        
# p1 = Person('Anmas' , 23)
# p1.myfunc()
# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()
# class Person:
#     def __init__(mysillyobject, name , age):
#         mysillyobject.name = name
#         mysillyobject.age = age
        
        
#     def myfunc(output):
#         print("Hello, My name is " + output.name)
        
        
# x_1 = Person('Aminul Islam' , 25)
# x_1.myfunc()
# class Person:
#     def __inti__(self , name , age):
#         self.name = name
#         self.age = age
        
#     def myfunc(self):
#         print("Hello my name is " + self.name)
        
# p1 = Person("Aminul Islam" , 25)

# p1.age = 40

# print(p1.age)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)

# p1.age = 40

# print(p1.age)
# class Person:
#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age
        
#     def myfunc(self):
#         print("Hello my name is " + self.name)
        
        
# p1 = Person('Aminul' , 24)

# p1.age = 33
# print(p1.age)
# class Person:
#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age
        
#     def myfunc(self):
#         print("Hello my name is " + self.name)
        
# p1 = Person('aminul' , 23)

# del p1.age
# print(p1.name)
# class Person:
#     def __init__(self , name, age):
#         self.name = name 
#         self.age = age
        
#     def myfunc(self):
#         print(f"My name is {self.name} and i am {self.age} years old.")
        
# p1 = Person("Aminul Islam" , 25)
# # print(p1.name)
# # print(p1.age)
# p1.myfunc()
# def myfunc():
#     print("Hello programmer! How is going everything? Is that everything okay? Hopefully so that. Now I will discuss about Use the super() Function.Python also a super() function that will make the child class inherit all the methods and properties from its parent.By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.IN the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the__init__( function.Add a year parameter, and pass the correct year when creating an object.Add a method called welcome to the Student class:If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?")
    
# # print(myfunc())
# myfunc()
# class Parent:
#     lson = "Mosaraf Molla"
#     small_son = "Asraful Islam"
    
# class child(Parent):
#     small_child1= "Kalam Uddin"
#     large_son = "Rahim Uddin"
    
# p1 = child
# print(p1.lson)
# print(p1.small_child1)
# class Person:
#     def __init__(self, fname , lname):
#         self.first_name = fname
#         self.last_name = lname
        
#     def printname(self):
#         print(f"Hi my name is {self.first_name} and my brother is {self.last_name}.")
        
# #Use the Person class to create an object, and then execute the printname method:

# x = Person("Aminul Islam" , "Ashraful Islam")

# x.printname()
# class Person:
#     def __init__(self , fname , lname):
#         self.firstname = fname
#         self.lastname = lname
        
#     def printname(self):
#         print(self.firstname , self.lastname)
        
# class Student(Person):
#     pass
# p1 = Student("Mike" , "Olsan")
# p1.printname()
# x = "Hello World"

# print(len(x))
# mytuple = ("apple" , 'banana' , "cherry")

# print(len(mytuple))
# thisdict = {
#     "brand": "Ford",
#     "model": 'Musting',
#     "year": 1997,
#     "id": 1213-121-12
# }


# print(len(thisdict))
# class Car:
#     def __init__(self , brand , model):
#         self.brand = brand 
#         self.model = model
        
#     def move(self):
#         print("Drive!")
        
# class Boat:
#     def __init__(self, brand , model):
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#         print("Sail!")
        
# class Plane:
#     def __init__(self, brand ,model):
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#         print("Fly!")
        
        
# car1 = Car("Ford" , "Musting") #Create a Car class
# Boat1 = Boat("Ibzia" , "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing " , "324") #Create a Plane class

# for x in (car1 , Boat1 , plane1):
#     x.move()
#Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes.
# class Car:
#     def __init__(self, brand , model):
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#         print("Drive!")
        
# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#         print("Sail!")
        
# class Plane:
#     def __init__(self, brand , model):
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#         print("Fly!")
        
# car1 = Car("Motor-Cycle" , "R15")
# boat1 = Boat("Steel-Body!" , "Stailness-Steel")
# plane1 = Plane("Hellicoptar" , "Mini-4")

# for x in (car1 , boat1, plane1):
#     x.move()
# class Vehicle:
#     def __init__(self, brand , model):
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#         print("Move!")
        
# class Car(Vehicle):
#      pass
 
# class Boat(Vehicle):
     
#      def move(self):
#          print("Sail!")
         

# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")
        
# car1 = Car("Ford" , "Musting")
# Boat1 = Boat("Ibzia" , "Touring 23")
# plane1 = Plane("Boeing" , "3234")


# for x in (car1 , Boat1 , plane1):
#     print(x.brand)
#     print(x.model)
    
# x.move()
class Vehicle:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Move!")
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")
        
class Plane(Vehicle):
    def move(self):
        print("Fly!")
        
car1 = Car("Ford" , "Musting")
boat = Boat("Ibtizia" , "Touring 23")
plane = Plane("Helicopter" , "Mini-Version-4")

for x in (car1 , boat , plane):
    print(x.brand)
    print(x.model)
    
    x.move()