# Program to print the digit '2' using stars (*) in a pattern of size n

n = int(input("Enter the value of n: "))                # Input size of the digit

for i in range(1, n + 1):                                # Loop through rows for top part
    for j in range(1, n + 1):                            # Loop through columns
        if j == n or i == 1 or i == n:                  # Print stars on last column, first and last row
            print("*", end=" ")                          # Print star with space
        else:
            print(" ", end=" ")                          # Print space inside hollow area
    print()                                              # New line after each row

for i in range(1, n):                                    # Loop through rows for bottom part
    for j in range(1, n + 1):                            # Loop through columns
        if i == n - 1 or j == 1:                         # Print stars on second last row and first column
            print("*", end=" ")                          # Print star with space
        else:
            print(" ", end=" ")                          # Print space inside hollow area
    print()                                              # New line after each row
