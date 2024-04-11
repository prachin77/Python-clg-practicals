if __name__ == "__main__":
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    year = input("> Enter Year: ")
    day = int(input("> Enter Day [0~6] [Mon ~ Sun]: "))

    firstDay = 0
    curmonth = 0  # Changed to start from 0 index for months
    month = ["Jan", "Feb", "March", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

    print("First Days Of the Months Are ~")
    print(f"Jan {days[day]}")

    num_of_days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Adjusted the number of days for each month
    for num in num_of_days_month:
        day = (day + num) % 7  
        print(f'{month[curmonth]} {days[day]}')
        curmonth += 1
