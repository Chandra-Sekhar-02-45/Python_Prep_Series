# This program determines the day of the week after a given number of days from a specified starting day.
# It assigns numerical values to days, applies modular arithmetic to handle the week cycle, and outputs the corresponding future day

print("\nThe input day should be in the format: Monday, Tuesday, etc., and 'n' should be between 1 and 31.")

d = input("Enter the day of the Week, Where you want to start the Month: ")
n = int(input("Enter the number of days to find the corresponding day of the week: "))

count = n % 7

if d == "Monday":
    day = 1
elif d == "Tuesday":
    day = 2
elif d == "Wednesday":
    day = 3
elif d == "Thursday":
    day = 4
elif d == "Friday":
    day = 5
elif d == "Saturday":
    day = 6
elif d == "Sunday":
    day = 0  

week = (day + count - 1) % 7

if week == 1:
    print(f"If the month starts with {d}, then the day after {n} days will be " + "Monday.")
elif week == 2:
    print(f"If the month starts with {d}, then the day after {n} days will be " + "Tuesday.")
elif week == 3:
    print(f"If the month starts with {d}, then the day after {n} days will be " + "Wednesday")
elif week == 4:
    print(f"If the month starts with {d}, then the day after {n} days will be " + "Thursday")
elif week == 5:
    print(f"If the month starts with {d}, then the day after {n} days will be " + "Friday")
elif week == 6:
    print(f"If the month starts with {d}, then the day after {n} days will be " + "Saturday")
elif week == 0:
    print(f"If the month starts with {d}, then the day after {n} days will be " + "Sunday")
