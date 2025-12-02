# program to find if a number is an armstrong number

# take input from the user
number = int(input("input your number:"))
# calculate number of digits
digits = len(str(number))
# initalize result variable
resultnumber = 0
# find sum of the a^digits of each digit 
temp = number 
while temp > 0:
    digit = temp % 10
    resultnumber += digit ** digits
    temp //= 10
# display the result
if number == resultnumber:
   print(number,"is an armstrong number")
else:
   print(number,"is not an armstrong number")