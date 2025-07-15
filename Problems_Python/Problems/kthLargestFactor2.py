# Program to print the k-th largest factor of a number n, or 1 if it does not exist

n = int(input("Enter the number (n): "))                          # Read the number n
k = int(input("Enter the value of k: "))                          # Read the value of k

count = 0                                                          # Counter for number of factors

for i in range(1, n + 1):                                          # Loop to count total factors of n
    if n % i == 0:
        count += 1                                                 # Increment factor count

n_factor = count                                                   # Total number of factors

if k >= n_factor:                                                  # If k-th largest factor does not exist
    print(1)                                                        # Print 1 as fallback
else:
    count = 0                                                       # Reset counter
    for i in range(1, n + 1):                                       # Loop to find (n_factor - k + 1)-th factor
        if n % i == 0:
            count += 1                                              # Increment factor count
            if count == n_factor - k + 1:                           # Check for required factor position
                print(i)                                            # Print the k-th largest factor
