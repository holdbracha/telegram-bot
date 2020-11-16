from math import ceil, sqrt
from sql_utils import get_popular_input_number

def isPrime(num):
    if num % 2 == 0:
        return "Come on dude, you know even numbers are not prime!"
    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0:
            return str(num) + ' is not prime'
    return str(num) + ' is prime'

def is_palindrome(input):
    input = str(input)
    reversedInput = input[::-1]
    if input == reversedInput:
        return input + " is palindrome"
    else:
        return input + " is not palindrome"

def is_factorial(input):
    org_input = input
    num = 2;
    while input > 1:
        if input % num != 0:
            return str(org_input) + " is not result of factorial operation"
        else:
            input /= num
            num += 1
    return str(org_input) + " is result of factorial operation: " + str(num - 1) + "!"

def has_int_sqrt(input):
    if sqrt(input) % 2 == 0:
        return "There is a sqrt root for " + str(input) + ": " + str(sqrt(input))
    return "There is not sqrt root for " + str(input)

def get_popular_in_number(input):
    return "The popular input number is {}".format(get_popular_input_number())

operations = {
    "/prime": isPrime,
    "/palindrome": is_palindrome,
    "/factorial": is_factorial,
    "/sqrt": has_int_sqrt,
    "/popular": get_popular_in_number
}

def getAction(operation, value):
    if operation not in operations.keys():
        return "invalid operation"
    return operations[operation](int(value))