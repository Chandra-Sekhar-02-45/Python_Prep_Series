# Read the number of rows for the diamond pattern
n = int(input("Enter the number of rows: "))

# -------- Upper half of the diamond --------
for row in range(n):                             # Loop from 0 to n-1 for the upper half
    print(" " * (n - row - 1), end="")            # Print leading spaces
    for col in range(row + 1):                    # Print stars in increasing order
        print("*", end=" ")                       # Print star followed by space
    print()                                       # Move to next line

# -------- Lower half of the diamond --------
for row in range(1, n):                           # Loop from 1 to n-1 for the lower half
    print(" " * row, end="")                      # Print increasing leading spaces
    for col in range(n - row):                    # Print stars in decreasing order
        print("*", end=" ")                       # Print star followed by space
    print()                                       # Move to next line
