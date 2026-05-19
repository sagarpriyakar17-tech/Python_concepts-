# Conditionals and Loops

# Conditionals help the program make decisions

name = "Sagar"
age = 19
college = "NHCK"
course = "BCA"


# Checking age using if elif else

if age < 13:
    print("You are a child")

elif age < 18:
    print("You are a teenager")

else:
    print("You are an adult")


# Short form condition

# If the score is greater than or equal to 50
# result becomes Pass otherwise Fail

score = 75

result = "Pass" if score >= 50 else "Fail"

print(result)


# Loops are used to repeat code


# for loop

# range(5) means numbers from 0 to 4

for i in range(5):

    print(i)


# Looping through a list

subjects = ["Python", "Cloud", "DevOps"]

# This loop prints each subject one by one

for subject in subjects:

    print(subject)


# while loop

# The loop keeps running while the condition is True

count = 0

while count < 3:

    print("Counting", count)

    # count increases by 1 each time

    count += 1


# break statement

# break stops the loop immediately

for i in range(10):

    if i == 4:
        break

    print(i)


# continue statement

# continue skips the current round

for i in range(5):

    if i == 2:
        continue

    print(i)


# enumerate function

# enumerate gives both index and value

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):

    print(index, fruit)


# Personal Information

print(f"My name is {name}")

print(f"I am {age} years old")

print(f"I study at {college}")

print(f"My course is {course}")
