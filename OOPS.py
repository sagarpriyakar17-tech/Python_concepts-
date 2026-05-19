# Object Oriented Programming

# OOP helps us organize code in a better way

# A class is like a blueprint

# An object is the real thing created from that blueprint

# Example

# Student can be a class
# Sagar can be an object of that class


# Class and Object

class Student:

    # init runs automatically when an object is created

    def __init__(self, name, age, college, course):

        self.name = name
        self.age = age
        self.college = college
        self.course = course


    # Method to display student details

    def info(self):

        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My college is {self.college}")
        print(f"My course is {self.course}")


    # Method for greeting

    def greet(self):

        print(f"Hello, I am {self.name}")


# Creating Objects

student1 = Student("Sagar", 19, "NHCK", "BCA")

student2 = Student("Rahul", 20, "NHCK", "BCA")


student1.greet()

student1.info()

student2.greet()


# Encapsulation

# Encapsulation means protecting data

# We use underscore to indicate
# that the variable should not be changed directly

class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner

        self._balance = balance


    def deposit(self, amount):

        self._balance += amount

        print(f"Deposited {amount}")


    def withdraw(self, amount):

        if amount > self._balance:

            print("Insufficient balance")

        else:

            self._balance -= amount

            print(f"Withdrawn {amount}")


    def get_balance(self):

        return self._balance


account = BankAccount("Sagar", 5000)

account.deposit(1000)

account.withdraw(2000)

print(account.get_balance())


# Inheritance

# Inheritance allows one class
# to use properties and methods of another class

class Person:

    def __init__(self, name):

        self.name = name


    def speak(self):

        print(f"{self.name} is speaking")


class Teacher(Person):

    def speak(self):

        print(f"{self.name} is teaching Python")


class StudentPerson(Person):

    def speak(self):

        print(f"{self.name} is learning Python")


teacher = Teacher("Arun")

student = StudentPerson("Sagar")


teacher.speak()

student.speak()


# Polymorphism

# Same method name behaves differently

people = [Teacher("Kiran"), StudentPerson("Sagar")]

for person in people:

    person.speak()


# Class Variable and Instance Variable

class CollegeStudent:

    # Class variable

    college = "NHCK"


    def __init__(self, name, course):

        # Instance variables

        self.name = name

        self.course = course


s1 = CollegeStudent("Sagar", "BCA")

s2 = CollegeStudent("Rahul", "BCA")


print(s1.college)

print(s1.name)

print(s2.name)


# Final Message

print("OOP helps make programs cleaner and easier to manage")
