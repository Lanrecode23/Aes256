class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

    def exponentiate(self, a, b):
        return a ** b

def main():
    calc = Calculator()
    
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiate")
        print("6. Exit")
        
        choice = input("Select an operation (1/2/3/4/5/6): ")
        
        if choice == '6':
            print("Exiting...")
            break
        
        if choice in {'1', '2', '3', '4', '5'}:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            
            if choice == '1':
                result = calc.add(num1, num2)
            elif choice == '2':
                result = calc.subtract(num1, num2)
            elif choice == '3':
                result = calc.multiply(num1, num2)
            elif choice == '4':
                result = calc.divide(num1, num2)
            elif choice == '5':
                result = calc.exponentiate(num1, num2)
            
            print(f"Result: {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()
