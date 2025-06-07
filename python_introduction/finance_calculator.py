
monthly_income = float(input("Enter your monthly income: "))  # Input for monthly income
total_expenses = float(input("Enter your total monthly expenses: "))  # Input for total monthly expenses

# Calculate monthly savings
monthly_savings = (monthly_income)-(total_expenses)  # Calculation for monthly savings

# Projected annual savings with a fixed interest rate of 5%
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)  # Annual savings calculation

# Output Results
print(f"Your monthly savings are: ${monthly_savings:.2f}.")  # Display monthly savings
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")  # Display projected annual savings
