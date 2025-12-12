# --- 1. Prompt for Task Details ---
task = input("Enter your task: ").lower()

# --- 2. Input Validation Loop ---
# Use a while loop to force the user to enter a valid priority
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

time_bound = input("Is it time-bound? (yes/no): ").lower()

# --- 3. Process and Provide Customized Reminder (using Match Case) ---
reminder_prefix = "Reminder:"
reminder_message = ""

match priority:
    case "high":
        if time_bound == "yes":
            # Instruction-specific message: 'that requires immediate attention today!'
            reminder_message = f"'{task}' is a high priority task that requires immediate attention today!"
        elif time_bound == "no":
            reminder_message = f"'{task}' is a high priority task. Plan time to get it done before it becomes urgent."
        else:
            # Handle invalid time_bound input within a valid priority
            reminder_message = f"'{task}' is a high priority task. Invalid time-bound response. Please prioritize it soon."
    
    case "medium":
        if time_bound == "yes":
            reminder_message = f"'{task}' is a medium priority task. Add a plan to complete it soon."
        elif time_bound == "no":
            reminder_message = f"'{task}' is a medium priority task. Plan a time to get this done this week."
        else:
            reminder_message = f"'{task}' is a medium priority task. Invalid time-bound response."

    case "low":
        if time_bound == "yes":
            reminder_message = f"'{task}' is a low priority task. Consider completing it just on time."
        elif time_bound == "no":
            # Instruction-specific note: 'Note: ' instead of 'Reminder: ' in the second example
            reminder_prefix = "Note:"
            reminder_message = f"'{task}' is a low priority task. Consider completing it when you have free time."
        else:
            reminder_message = f"'{task}' is a low priority task. Invalid time-bound response."
    
    # Note: The while loop handles invalid priority input before reaching this point, 
    # but a generic case is kept for completeness in Match Case structures.
    case _:
        reminder_message = "Error processing task priority."


# --- 4. Final Output ---
# Print the required prefix and the resulting message
print(f"\n{reminder_prefix} {reminder_message}")