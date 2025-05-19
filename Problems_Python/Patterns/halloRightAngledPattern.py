n = int(input("Enter the number of rows : "))  # Read input number of rows

for i in range(1, n + 1):  # Loop through rows from 1 to n
    for j in range(1, i + 1):  # Loop through columns from 1 to current row number

        if i == j or i == n:  # Print number if it's the end of the row or last row
            print(j, end=" ")

        elif j == 1:  # Always print '1' at the start of the row
            print(1, end=" ")

        else:  # Print spaces between the start and end
            print("  ", end="")  # Two spaces for alignment

    print()  # Move to the next line after each row
