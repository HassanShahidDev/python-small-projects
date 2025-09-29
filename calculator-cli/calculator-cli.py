# calculator-cli.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def calculator():
    print("Welcome to CLI Calculator!")
    while True:
        print("\nSelect operation: +, -, *, / or 'q' to quit")
        choice = input("Enter operation: ")
        if choice == 'q':
            print("Goodbye!")
            break
        if choice in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == '+':
                print("Result:", add(num1, num2))
            elif choice == '-':
                print("Result:", subtract(num1, num2))
            elif choice == '*':
                print("Result:", multiply(num1, num2))
            elif choice == '/':
                print("Result:", divide(num1, num2))
        else:
            print("Invalid operation!")

if __name__ == "__main__":
    calculator()
