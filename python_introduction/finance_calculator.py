# Define variables

year_to_add = 27

# Prompt the user for their monthly income

monthly_income_input = input ("Enter your monthly income:")
monthly_income = int(monthly_income_input)

# Prompt the user for their total monthly expenses

total_monthly_expenses_input = input ("Enter your total monthly expenses:")
total_monthly_expenses = int(total_monthly_expenses_input)

# Calculate Monthly Savings

monthly_savings = monthly_income - total_monthly_expenses

# Calculate Project Annual Savings

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print the final result
print(f"Your monthly saving are {monthly_income}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")