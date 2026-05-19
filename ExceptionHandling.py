# Exception Handling

# Errors can happen while running a program

# If we do not handle errors
# the program may suddenly stop

# Exception handling helps us control errors
# and keep the program running smoothly


# Example without exception handling

# This would crash the program

# print(10 / 0)


# Basic try and except

# try contains the risky code
# except runs if an error happens

try:

    result = 10 / 0

except ZeroDivisionError:

    print("You cannot divide a number by zero")


# Handling invalid input

# int only accepts numbers
# converting text like hello causes ValueError

try:

    number = int("hello")

except ValueError:

    print("Please enter a valid number")


# else block

# else runs only if no error occurs

try:

    result = 10 / 2

except ZeroDivisionError:

    print("Error happened")

else:

    print("Program ran successfully")
    print("Result is", result)


# finally block

# finally always runs
# even if there is an error

try:

    result = 10 / 0

except ZeroDivisionError:

    print("Error was handled")

finally:

    print("This block always executes")


# Catching any type of error

# Exception catches almost all errors

try:

    x = int(input("Enter a number: "))

    print(10 / x)

except Exception as e:

    print("Something went wrong")
    print(e)


# Raising your own error

# raise is used when we want to create a custom error

def check_age(age):

    if age < 0:

        raise ValueError("Age cannot be negative")

    print("Age is", age)


try:

    check_age(-5)

except ValueError as e:

    print(e)


# Common Exception Types

# ZeroDivisionError happens when dividing by zero

# ValueError happens when the value is invalid

# TypeError happens when wrong data types are used together

# IndexError happens when list index does not exist

# KeyError happens when a dictionary key is missing

# FileNotFoundError happens when a file cannot be found


# Real Life Example

# Imagine a login system

# If the user enters wrong data
# the program should not crash

# Instead it should show a proper message
# and ask the user to try again

