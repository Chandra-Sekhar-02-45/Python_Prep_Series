# Program to check whether a given year is a leap year or not

year = int(input("Enter the year: "))                    # Take input year from the user

if year % 4 == 0:                                        # Check if divisible by 4
    if year % 100 == 0:                                  # If divisible by 100, check further
        if year % 400 == 0:                              # If divisible by 400, it's a leap year
            print(str(year) + " is a Leap Year")         # Leap year if divisible by 400
        else:
            print(str(year) + " is not a Leap Year")       # Not a leap year if not divisible by 400
    else:
        print(str(year) + " is a Leap Year")             # Leap year if not divisible by 100
else:
    print(str(year) + " is not a Leap Year")               # Not a leap year if not divisible by 4
