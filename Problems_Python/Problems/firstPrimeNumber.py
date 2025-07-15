# Program to read n numbers and print the first prime number entered

n = int(input("Enter the number of inputs (n): "))                  # Read the number of inputs to process

while n > 0:                                                         # Loop until n becomes 0
    m = int(input("Enter a number: "))                              # Read the next number
    count = 0                                                        # Counter for factors of m

    for i in range(1, m + 1):                                        # Loop to count factors of m
        if m % i == 0:
            count += 1                                               # Increment factor count

    if count == 2:                                                   # Check if m is a prime number
        print("First prime number entered:", m)                      # Print the prime number
        break                                                        # Exit the loop when first prime is found

    n -= 1                                                           # Decrement the count of inputs left
