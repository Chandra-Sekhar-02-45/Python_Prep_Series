# Read the number of rows for the diamond pattern
n = int(input("Enter the number of rows: "))

# -------- Upper half of the diamond --------
for row in range(n):                             # Loop from 0 to n-1 for the upper half
    print(" " * (n - row - 1), end="")            # Print spaces to align numbers to center
    count = 1                                     # Initialize number count
    for col in range(row + 1):                    # Loop to print numbers from 1 to row+1
        print(count, end=" ")                     # Print the current number
        count += 1                                # Increment number
    print()                                       # Move to the next line

# -------- Lower half of the diamond --------
for row in range(1, n):                           # Loop from 1 to n-1 for the lower half
    print(" " * row, end="")                      # Print increasing spaces from top to bottom
    count = 1                                     # Initialize number count
    for col in range(n - row):                    # Loop to print decreasing number of values
        print(count, end=" ")                     # Print the current number
        count += 1                                # Increment number
    print()                                       # Move to the next line
