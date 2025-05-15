n = int(input("Enter the number of rows: "))         # Take input for the number of rows

for i in range(n):                                   # Outer loop for each row
    count = 0                                        # Reset count at the beginning of each row

    for j in range(n - i):                           # Inner loop to control decreasing elements per row
        count += 1                                   # Increment the counter
        print(count, end=" ")                        # Print the current count followed by a space

    print()                                          # Print a newline after each row
