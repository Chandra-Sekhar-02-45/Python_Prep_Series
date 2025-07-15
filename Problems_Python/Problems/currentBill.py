units = int(input("Enter the number of units: "))

if units >= 0 and units <= 50 :
    charge = (units - 0) * 2
    tax = charge * 0.2
    bill = charge + tax
    print("Your bill is $", bill)
elif units > 50 and units <= 150 :
    charge = (50 * 2) + ((units - 50) * 3)
    tax = charge * 0.2
    bill = charge + tax
    print("Your bill is $", bill)
elif units > 150 and units <= 250:
    charge = (50 * 2) + (100 * 3) + ((units - 150) * 5)
    tax = charge * 0.2
    bill = charge + tax
    print("Your bill is $", bill)
elif units > 250:
    charge = (50 * 2) + (100 * 3) + (100 * 5) + ((units - 250) * 8)
    tax = charge * 0.2
    bill = tax + charge
    print("Your bill is $", bill)
