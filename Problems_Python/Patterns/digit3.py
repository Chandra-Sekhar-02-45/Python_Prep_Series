# Program to print the digit '3' using stars (*) in a pattern of size n

n = int(input("Enter the value of n: "))                  # Input size of the digit

for i in range(1, 2 * n):                                  # Loop through rows from 1 to 2n-1
    for j in range(1, n + 1):                              # Loop through columns from 1 to n
        # Print stars on first row, middle row, last row, and last column
        if i == 1 or i == n or i == (2 * n - 1) or j == n:
            print("* ", end="")                            # Print star with space
        else:
            print("  ", end="")                            # Print spaces for hollow area (2 spaces for alignment)
    print()                                                # New line after each row
