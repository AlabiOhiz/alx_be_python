# Define variables

year_to_add = 27

# Prompt the user for their current age

current_age_input = input ("How old are you?")
current_age = int (current_age_input)

# Calculate the age 

age_in_2050 = current_age + year_to_add

# Print the final result in the specified format using an f-string
print("In 2050, you will be {age_in_2050} years old.")