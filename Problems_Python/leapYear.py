year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a Leap Year")
        else:
            print(str(year)+" is not Leap Year")
    else:
        print(str(year)+" is a Leap Year")
else:
    print(str(year)+" is not Leap Year")
