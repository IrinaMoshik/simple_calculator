def divide(a, b):
    if b == 0:
        return 'Error! Division by zero is not allowed.'
    else:
        return a / b

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
print('Result:', divide(num1, num2))