# #Simple exception handling 
# try:
#     a= int (input("Enter the number: "))
#     b=100/a
# except ZeroDivisionError:
#     print("OOPS ! cannot be divisible by zero")
# except ValueError:
#     print("Please enter the valid number")
# finally:
#     print("This always runs......:)")
    
    
# #raise you own exception

# age = 12
# if age<18:
#     raise Exception("You are not elligible...!")

"""
🎓 Mini Challenge
Write a program that takes a number input and:

Raises a custom exception if it's negative.

Handles the case if the input is not a number.

Always prints "Done with processing!" at the end.
"""
try:
    number = int(input("Please Enter your ticket number: "))
    if number<0:
        raise Exception("Sorry:( the ticket number cannot be negative")
except ValueError:
    print("Please enter the valid number")
else:
    print("Your ticket is valid and good to go")
finally:
    print("Enjoy your show!")