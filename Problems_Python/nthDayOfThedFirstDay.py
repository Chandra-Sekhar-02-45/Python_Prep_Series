# In this given code 

d = input("Enter the day of the Week, Where you want to start the Month")
n = int(input("Enter the number of days to find the corresponding day of the week:")) % 7  

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
else:
    day = 0  

week = (day + n - 1) % 7  

if week == 1:
    print("Monday")
elif week == 2:
    print("Tuesday")
elif week == 3:
    print("Wednesday")
elif week == 4:
    print("Thursday")
elif week == 5:
    print("Friday")
elif week == 6:
    print("Saturday")
else:
    print("Sunday")
