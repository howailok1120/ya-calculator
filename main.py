from datetime import datetime
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

while True:
    date_input = input("Enter year-end date (dd/mm/yyyy): ")

    # Convert the input string to a datetime object
    input_date = datetime.strptime(date_input, "%d/%m/%Y")

    # Extract the month value from the input date
    input_month = input_date.strftime("%b")  # Returns the abbreviated month name

    # Extract the year value from the input date
    input_year = input_date.year

    # Define the start and end dates for the comparison
    start_date_m_code = datetime(2023, 1, 1)
    end_date_m_code = datetime(2023, 3, 31)
    start_date_d_code = datetime(2023, 12, 1)
    end_date_d_code = datetime(2023, 12, 31)

    # Perform the date comparison
    if start_date_m_code <= input_date <= end_date_m_code:
        print("")
        print(f"Result: 'M Code', the standard deadline should be 15 Nov {input_year}")
        print(f"Adjusted loss could extended to 31 Jan {input_year}")
        print("")
        
    elif start_date_d_code <= input_date <= end_date_d_code:
        print("")
        print(f"Result: 'D Code', the standard deadline should be 15 Aug {input_year + 1}")
        print("Loss extension not available")
        print("")
    else:
        print("")
        print(f"Result: 'N Code', the standard deadline should be 30 Apr {input_year + 1}")
        print("Loss extension not available")
        print("")

    continue_input = input("Do you want to continue? (y/n): ")
    if continue_input.lower() != "y":
        break

    clear()