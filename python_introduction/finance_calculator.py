

# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
total_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - total_expenses

# Projected annual savings with a fixed interest rate of 5%
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Output Results
print(f"Your monthly savings are: ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
