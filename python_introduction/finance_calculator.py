def get_float_input(prompt):
    """Function to get a float input from the user with error handling."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    # User Input for Financial Details
    monthly_income = get_float_input("Enter your monthly income: ")
    total_expenses = get_float_input("Enter your total monthly expenses: ")

    # Calculate monthly savings
    monthly_savings = monthly_income - total_expenses

    # Output Results
    if monthly_savings < 0:
        print("Warning: Your expenses exceed your income. You have negative savings.")
    else:
        print(f"Your monthly savings are: ${monthly_savings:.2f}.")

if __name__ == "__main__":
    main()
