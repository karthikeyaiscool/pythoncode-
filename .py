# to find factors of user input

# goes from 1 to number and check if I divide If yes it is a factor
def print_factors(number):
    print("the factors of",number,"are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
# takeing input from the user
number = int(input("enter your number to find its factors: "))

# calling our function
print_factors(number)