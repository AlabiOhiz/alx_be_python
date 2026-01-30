from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains the current date and time and prints it in a readable format.
    """
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    # Formatting the date: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for days, calculates, and prints the future date.
    """
    try:
        # Prompting user for the number of days
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        
        # Part 2: Calculate a Future Date
        future_date = current_date + timedelta(days=number_of_days)
        
        # Formatting the future date: YYYY-MM-DD
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
        return future_date
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

def main():
    # Call the functions
    current_dt = display_current_datetime()
    calculate_future_date(current_dt)

if __name__ == "__main__":
    main()