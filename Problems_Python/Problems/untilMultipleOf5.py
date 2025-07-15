# Program to read n numbers and print them until a number divisible by 5 is entered

n = int(input("Enter the number of inputs (n): "))                     # Read the number of inputs to process

while n > 0:                                                            # Loop until n becomes 0
    m = int(input("Enter a number: "))                                  # Read the next number

    if m % 5 == 0:                                                       # Check if number is divisible by 5
        break                                                            # Exit the loop if divisible by 5
    else:
        print("Number entered (not divisible by 5):", m)                 # Print number if not divisible by 5

    n -= 1                                                               # Decrement the count of inputs left
