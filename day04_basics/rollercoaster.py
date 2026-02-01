print("Roller Coaster ticket system")
height = int(input("What is your height in cm?"))
bill = 0
if height >=120:
    print("You can ride!")
    age = int(input("What is your age?"))

    if age >=18:
        bill = int(10)
        print(f"You will pay {bill} dollars!")
    elif age <=12:
        bill = 3
        print(f"You will pay {bill} dollars!")
    else:
        bill = 5
        print(f"You will pay {bill} dollars!")
    wants_photo = input("Do you want a photo for an extra $3? y if yes, n if no...")
    if wants_photo == "y":
        print(f"Your bill is {bill+3} dollars..")
    else:
        print(f"Your bill is {bill} dollars..")
else:
    print("You cannot ride!")
# What I learned up to Day 3 of Angela Yu's "100 Days of Code" Python course:
#
# From Day 1 to Day 3, I learned many core Python basics such as:
# string manipulation, variables, input() function, primitive data types,
# mathematical operations, modulo operator, and if / else conditional logic
# including nested if statements and elif.
#
# I also practiced debugging a lot. This helped me understand how to search
# for errors properly and use online resources to quickly fix problems
# when my code did not work as expected.
#
# About input():
# Using the input() function, I can ask questions to the user and use
# their answers inside the program.
#
# About variables:
# I see variables as named boxes that store data. They help me write
# cleaner, more readable, and easier-to-manage code.
#
# About primitive data types:
# - String (str): used for text
# - Integer (int): used for whole numbers
# - Float (float): used for decimal numbers like 13.54
# - Boolean (bool): used for logical results (True or False)
#
# I also learned how to use f-strings, which make printing values
# much cleaner and easier to read.
# Example: f"Your total bill is ${price}"
#
# At the end of Day 3, I paused the course and wrote the
# "Roller Coaster Ticket System" program by myself.
# After comparing my solution with Angela Yu's version,
# I realized that I was able to use the concepts correctly
# and make the program run successfully.
