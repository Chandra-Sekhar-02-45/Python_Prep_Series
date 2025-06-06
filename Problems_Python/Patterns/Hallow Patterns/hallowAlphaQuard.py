# Program to print a rectangular pattern using alphabets with hollow middle rows

m = int(input("Enter the number of rows (m): "))          # Input total number of rows
n = int(input("Enter the number of columns (n): "))       # Input total number of columns
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                     # Reference string of alphabets
count = 0                                                 # Counter to track current letter index
sp = 2 * n - 3                                            # Space count for hollow rows

for i in range(m):                                        # Loop through each row
    row = ""                                              # Initialize an empty row string
    for j in range(n):                                    # Loop through each column
        if i == 0 or i == (m - 1):                         # First or last row
            row += string[count] + " "                     # Add character followed by space
        elif j == 0:                                       # First column of hollow row
            row += string[count] + " " * sp + string[n + count - 1]  # Left char + spaces + right char
        count += 1                                         # Increment letter index
    print(row)                                             # Print the current row
