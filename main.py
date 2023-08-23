# 1) YE: 31 Dec 2023
# Answer: YA 2023/24
# PTR Submission Deadline: 15 Aug 2024

# 2) YE: 31 Mar 2023
# Answer: YA 2022/23
# PTR Submission Deadline: 15 Nov 2023

# 3) YE: 30 May 2023
# Answer: YA 2023/24
# PTR Submission Deadline: 15 Nov 2023

# 4) YE: 1 Apr 2023
# Answer: YA 2023/24
# PTR Submission Deadline: 30 Apr 2023 

# 5) 31 Mar 2023 with adjusted loss
# Answer: YA 2022/23
# PTR Submission Deadline: 31 Jan 2024

# 6) 1st PTR 
# PTR Submission Deadline 3 months after issue date of PTR


from datetime import datetime
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

while True:
    print("PTR Year of Assessment Calculator with standard submission deadline.")
    print("Created by Leo Ho, all rights reserved under MIT License.")
    print("Github: https://github.com/howailok1120")
    print("")
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