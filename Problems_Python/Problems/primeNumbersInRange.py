# Taught On Approach:

m = int(input("Enter the starting number (m): "))  # Take input from the user for the starting number
n = int(input("Enter the ending number (n): "))    # Take input from the user for the ending number

is_Prime = False                                   # Initialize a flag to track if any prime numbers are found

for i in range(m, n + 1):                          # Loop through each number in the range from m to n (inclusive)

    if i < 2:
        continue                                   # Skip numbers less than 2 (not prime)

    count = 0                                      # Init a counter

    for j in range(2, i):                          # Check for factors from 2 to i-1
        if i % j == 0:
            count += 1                             # If a factor is found, increment count

    if count == 0:
        print(i, end=" ")                          # If no factors were found, it's a prime number — print it
        is_Prime = True                            # Set flag to True, as a prime number was found

if not is_Prime:
    print("No Prime Numbers Found")                # If no prime numbers were printed, show this message
