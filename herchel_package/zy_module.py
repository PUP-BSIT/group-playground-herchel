import calendar

def show_month_calendar():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    
    print(f"\nCalendar for {year} {month}: " )
    print(calendar.month(year, month))

def is_leap_year():
    year = int(input("Enter a year to check if it's a leap year: "))
    
    # Check and display whether the year is a leap year
    if calendar.isleap(year):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year.")
