
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
    monthly_income = get_float_input("Enter your monthly income: ")  # Input for monthly income
    total_expenses = get_float_input("Enter your total monthly expenses: ")  # Input for total monthly expenses

    # Calculate monthly savings
    monthly_savings = monthly_income - total_expenses  # Calculation for monthly savings

    # Check if savings are negative
    if monthly_savings < 0:
        print("Warning: Your expenses exceed your income. You have negative savings.")
    else:
        # Projected annual savings with a fixed interest rate of 5%
        projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)  # Annual savings calculation

        # Output Results
        print(f"Your monthly savings are: ${monthly_savings:.2f}.")  # Display monthly savings
        print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")  # Display projected annual savings

if __name__ == "__main__":
    main()
