"""
🧪 Task: Age Verifier App
Ask the user’s age and:
If not a number ➝ handle it
If age < 0 ➝ raise error
If age < 18 ➝ print “Too young to vote”
Else ➝ print “Welcome to the system”
Finally ➝ always print "Done!"
"""

try:
    age=int(input("Enter the age: "))
    if age<0:
        raise Exception("Opps!...You are not born yet")
    elif age<18:
        print("Too young to vote")
    else:
        print("Welcome to the system")
except ValueError:
    print("Please enter the valid age in numbers")
finally:
    print("Done!")
    
# class NegativeNumberError(Exception):
#     pass

# num = int(input("Enter a number: "))
# if num < 0:
#     raise NegativeNumberError("Negative numbers are not allowed!")
