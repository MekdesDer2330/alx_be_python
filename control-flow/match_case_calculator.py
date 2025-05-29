

# Function to perform calculations using Match Case
def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Cannot divide by zero."
            else:
                return num1 / num2
        case _:
            return "Invalid operation."

# Main function to run the calculator
def main():
    # Prompt for user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")

        # Perform calculation and get the result
        result = calculate(num1, num2, operation)

        # Output the result
        if isinstance(result, str):
            print(result)  # Print error messages
        else:
            print(f"The result is {result}.")
    
    except ValueError:
        print("Please enter valid numbers.")

# Run the main function
if __name__ == "__main__":
    main()
