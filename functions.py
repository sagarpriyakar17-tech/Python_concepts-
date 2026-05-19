# Functions

# Functions are reusable blocks of code

# Instead of writing the same code again and again
# we can create a function and use it whenever needed


# Basic Function

def greet():

    print("Hello Sagar, welcome to Python")


# Calling the function

greet()


# Function with Parameters

# Parameters allow us to pass values into a function

def greet_user(name):

    print(f"Hello {name}")


greet_user("Sagar")

greet_user("Rahul")


# Function with Return Value

# return sends the result back

def add(a, b):

    return a + b


result = add(3, 7)

print(result)


# Default Parameters

# If no value is given
# the default value will be used

def student_info(name="Student"):

    print(f"Welcome {name}")


student_info()

student_info("Sagar")


# Returning Multiple Values

def stats(numbers):

    return min(numbers), max(numbers), sum(numbers)


low, high, total = stats([4, 7, 1, 9, 3])

print(low, high, total)


# args

# args allows multiple values to be passed

def add_all(*numbers):

    return sum(numbers)


print(add_all(1, 2, 3))

print(add_all(10, 20, 30, 40))


# Lambda Function

# Lambda is a small one line function

square = lambda x: x * x

print(square(5))


# Personal Example

def college_details(name, college, course):

    print(f"My name is {name}")
    print(f"I study at {college}")
    print(f"My course is {course}")


college_details("Sagar", "NHCK", "BCA")
