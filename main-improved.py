from datetime import datetime
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_deadline(date):
    input_date = datetime.strptime(date, "%d/%m/%Y")
    input_month_day = input_date.replace(year=2000)

    input_month = input_date.strftime("%b")
    input_year = input_date.year

    start_date_m_code = datetime(2000, 1, 1)
    end_date_m_code = datetime(2000, 3, 31)
    start_date_d_code = datetime(2000, 12, 1)
    end_date_d_code = datetime(2000, 12, 31)

    if start_date_m_code <= input_month_day <= end_date_m_code:
        return f"'M Code', the standard deadline should be 15 Nov {input_year}", f"Adjusted loss could be extended to 31 Jan {input_year}"
    elif start_date_d_code <= input_month_day <= end_date_d_code:
        return f"'D Code', the standard deadline should be 15 Aug {input_year + 1}", "Loss extension not available"
    else:
        return f"'N Code', the standard deadline should be 30 Apr {input_year + 1}", "Loss extension not available"

def main():
    clear()
    while True:
        print("PTR Year of Assessment Calculator with standard submission deadline.")
        print("Created by Leo Ho, all rights reserved under MIT License.")
        print("Github: https://github.com/howailok1120")
        print("")
        date_input = input("Enter year-end date (dd/mm/yyyy): ")

        result, loss_extension = calculate_deadline(date_input)
        print("")
        print("Result:", result)
        print(loss_extension)
        print("")

        continue_input = input("Do you want to continue? (y/n): ")
        if continue_input.lower() != "y":
            break

        clear()

if __name__ == "__main__":
    main()