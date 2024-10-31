# Reuben Stoutenburg
# UWYO COSC 1010
# Submission Date 10/31/2005
# Lab 07
# Lab Section: 16
# Sources, people worked with, help given to: w3schools.com, and my roomate
# your
# comments
# here

factorial = 1

while True:
    upper_bound = input("Enter a number and I will give you its factorial: ")

    if upper_bound.isdigit(): #check if input is a digit
        upper_bound = int(upper_bound)
        if upper_bound > 0: #check if number is greater than zero
            for i in range(1, upper_bound + 1):
                factorial *= i #loop through numbers up to the given upper bound
            break
        else:
            print("Please enter a positive number.") #if number isn't positive direct them to give a positive number
    else:
        print("Please enter a number.") #if they type anything but a number ask for a number
     
print(f"The result of the factorial based on the given bound is {factorial}")

print("*" * 75)

num_sum = 0

while True:
    numbers = input("Give me numbers and I will add them together('exit' to quit): ")
    if numbers.lower() == 'exit':
        break
    for num in numbers.split():
        if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
            numbers = int(num)
            num_sum += numbers
        else:
            print(f"{num} is not a valid integer, please try again.")

print(f"Your final sum is {num_sum}")
print("*" * 75)

def calculator():
    while True:
        value = input("Enter desired calculation (operand operator operand) or type 'exit' to quit: ").strip()
        if value.lower() == 'exit':
            break
        value = value.replace(' ', '')
        if '+' in value:
            operands = value.split('+')
            operator = '+'
        elif '-' in value:
            operands = value.split('-')
            operator = '-'
        elif '/' in value:
            operands = value.split('/')
            operator = '/'
        elif '*' in value:
            operands = value.split('*')
            operator = '*'
        elif '%' in value:
            operands = value.split('%')
            operator = '%'
        else:
            print("Invalid operator. Please try again.")
            continue
        if len(operands) == 2 and operands[0].isdigit() and operands[1].isdigit():
            operand1 = int(operands[0])
            operand2 = int(operands[1])
        else:
            print("Invalid input please try again.")
            continue
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            result = operand1 / operand2
        elif operator == '%':
            result = operand1 % operand2
        print(f"The result of {operand1} {operator} {operand2} is: {result}")
calculator()




        






