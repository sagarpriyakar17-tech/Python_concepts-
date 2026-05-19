# Variables and Data Types

# Variables are used to store values in Python.
# You can think of a variable like a containers,that stores some information.


# Creating Variables

name = "Sagar"      # string stores text
age = 25            # integer stores whole numbers
height = 5.9        # float stores decimal numbers
is_happy = True     # boolean stores True or False

# Printing Variables

print(name)
print(age)
print(height)
print(is_happy)

# Checking Data Types

print(type(name))       # class 'str'
print(type(age))        # class 'int'
print(type(height))     # <class 'float'
print(type(is_happy))   # class 'bool'

# None Type

# None means empty or no value

result = None
print(result)

# Multiple Variable Assignment

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# Type Conversion

# Converting string to integer
print(int("42"))

# Converting integer to float
print(float(10))

# Converting integer to string
print(str(100))

# Boolean conversion
print(bool(0))     # False
print(bool(99))    # True

# f-strings

# f-strings help combine text and variables easily

name = "Sagar"
age = 25

print(f"My name is {name} and I am {age} years old.")
