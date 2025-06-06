# Program to print a digit 8 pattern with stars (*) along the border

n = int(input("Enter the value of n: "))               # Take input for the size parameter

for i in range(1, 2 * n + 2):                          # Loop over rows from 1 to 2n+1 (inclusive)
    for j in range(1, n + 1):                          # Loop over columns from 1 to n (inclusive)
        # Print star if on first row, last row, middle row, or first/last column
        if i == 1 or j == 1 or j == n or i == (n + 1) or i == (2 * n + 1):
            print("* ", end="")                         # Print star with space, no newline
        else:
            print("  ", end="")                         # Print spaces for hollow part
    print()                                            # Move to next line after each row
