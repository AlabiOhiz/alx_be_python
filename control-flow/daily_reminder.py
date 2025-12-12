task = input("Enter your task: ").lower()

priority = input("Priority (high/medium/low):  ").lower()
time_bound = input("Is it time-bound? (yes/no):  ").lower()

# --- MODIFICATION START ---
print("\n--- Daily Task Reminder ---")
# --- MODIFICATION END ---

match priority:
    case "high":
        if time_bound == "yes":
            print(f" '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task}' is a high priority task that requires to create time get it done before it urgent!")
        else:
            print("Invaild Response")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task. Add a plan to get it done before it too late")
        elif time_bound == "no":
            print(f"'{task}' is a medium priority task. please plan a time to get this done")
        else:
            print("Invaild Response")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task. Consider completing it soon just on time")
        elif time_bound == "no":
            print(f" {task}  is a low priority task. Consider completing it when you have free time.")
        else:
            print("Invaild Response")
    case _:
        print("Invalid priority entered.")