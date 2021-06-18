
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

print('')
print('Comtraya! Please select math function:')
print('')
print('\033[31m 1. Addition')
print('\033[36m 2. Subtraction')
print('\033[35m 3. Multiplication')
print('\033[91m 4. Division')
    
while True:
    selection = input("\033[0mEnter choice: ")

    if selection in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if selection == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif selection == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif selection == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif selection == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
else:
    print("Invalid Input")