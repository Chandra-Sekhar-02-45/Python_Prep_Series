n = int(input())  # Read the number of rows from the user

for row_num in range(n):       # Loop from 0 to n-1, each iteration is one row
    row_output = ""            # Initialize an empty string to build the current row
    seq_num = n - row_num      # Start value for the current row (decreases each row)

    while seq_num > 0:         # Keep adding numbers until seq_num reaches 0
        row_output = row_output + str(seq_num) +  " "  # Append current number as string to row_output
        seq_num = seq_num - 1  # Decrease seq_num by 1 to move towards 1

    print(row_output)          # Print the completed row
