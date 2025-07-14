# Program to print the (k)th largest factor of a number 'n' if it exists, otherwise print 1

n = int(input("Enter the number (n): "))                             # Read the number n
k = int(input("Enter the number (k): "))                             # Read the value of k

count = 0                                                            # Counter for number of factors

for i in range(1, n + 1):                                            # Loop from 1 to n
    if n % i == 0:                                                   # Check if i is a factor of n
        count += 1                                                   # Increment factor count
        if count == k + 1:                                           # If (k+1)th factor is found
            print(k, "Largest Factor is:", i)                        # Print the (k+1)th factor
            break                                                    # Exit the loop

n_factor = count                                                     # Store total number of factors found

if k >= n_factor:                                                    # If (k+1)th factor doesn't exist
    print(k, "is greater than number of factors : 1")                # Print 1 as fallback result
