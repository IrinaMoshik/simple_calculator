
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b



num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
choice = input('Enter choice (1, 2, 3): ')
    
if choice == '1':
    print('Result:', add(num1, num2))
elif choice == '2':
    print('Result:', subtract(num1, num2))
elif choice == '3':
    print('Result:', multiply(num1, num2))
else:
    print('Invalid choice')


