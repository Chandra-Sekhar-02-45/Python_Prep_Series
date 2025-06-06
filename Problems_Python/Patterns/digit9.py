# Program to print the digit '9' using stars (*) in a pattern of size n

n = int(input("Enter the value of n: "))                  # Input size of the digit

for i in range(1, 2 * n):                                  # Loop through rows from 1 to 2n-1
    for j in range(1, n + 1):                              # Loop through columns from 1 to n
        # Print stars on first row, nth column, nth row,
        # last row (2n-1), and first column for rows <= n
        if i == 1 or j == n or i == n or i == (2 * n - 1) or (j == 1 and i <= n):
            print("* ", end="")                            # Print star with space
        else:
            print("  ", end="")                            # Print spaces for hollow area (2 spaces for alignment)
    print()                                                # New line after each row
