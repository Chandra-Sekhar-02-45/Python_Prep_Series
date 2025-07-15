# Program to print the kth Largest factor of m

m = int(input("Enter value of m: "))                         # Read the number m
n = int(input("Enter value of n: "))                         # Read the number n
count = 0                                                    # Initialize factor count

for i in range(1, m + 1):                                    # Count total number of factors of m
    if m % i == 0:
        count += 1

num = count - n + 1                                          # Compute the required factor position from beginning

count = 0                                                    # Reset count
for i in range(1, m + 1):                                    # Loop again to find the (count - n + 1)th factor
    if m % i == 0:
        count += 1
        if count == num:
            print("Result:", i)                              # Print the desired factor
