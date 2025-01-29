noDays = int(input("Enter the number of days: "))

year = noDays // 365             # ' // ' is floor division, which gives the quotient without the remainder
rem_weeks = noDays % 365
weeks = rem_weeks // 7           # ' // ' is floor division, which gives the quotient without the remainder
days = rem_weeks % 7

print(year, "Years", weeks, "Weeks", days, "Days")
