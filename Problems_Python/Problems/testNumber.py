number = int(input("Enter a number: "))


if number > 0:
    print(str(number)+ " is a Natural Number")
elif number == 0:
    print(str(number) + " is a Whole Number")
    print(str(number)+ " is a Non Negative Number")
else:
    print(str(number)+ " is a Negative Number")

"Checking the number is Even Number or Odd Number"
if number % 2 == 0:
    print(str(number) + " is an Even Number")
else:
    print(str(number) + " is an Odd Number")

"Checking the number is Prime Number"
if number == 2:
    print(str(number) + " is an EvenPrime Number")