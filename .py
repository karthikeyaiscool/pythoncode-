# take input from the user 
number = int(input("Enter your number: "))

# store the origanal number for comparison later
original_number = number
reversed_number = 0

# reverse the order
while number> 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit


# check if the origanal number and the reversed number are the same 
if original_number == reversed_number :
    print(f"{original_number} is a palindrone") 
else:
    print(f"{original_number} is not a palindrone") 
       