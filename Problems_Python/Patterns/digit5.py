# Program to print the digit '5' using stars (*) in a pattern of size n

n = int(input("Enter the value of n: "))                  # Input size of the digit

for i in range(1, 2 * n):                                  # Loop through rows from 1 to 2n-1
    for j in range(1, n + 1):                              # Loop through columns from 1 to n
        # Print stars on first, middle, and last rows,
        # first column for upper half, and last column for lower half
        if i == 1 or i == n or i == (2 * n - 1) or (j == 1 and i <= n) or (j == n and i >= n):
            print("*", end=" ")                            # Print star with space
        else:
            print(" ", end=" ")                            # Print spaces for hollow area
    print()                                                # New line after each row
