m = int(input())  # Number of columns
n = int(input())  # Number of rows

for i in range(1, m + 1):  # Loop through rows
    count = m + n  # Start number for each row

    for j in range(1, n + 1):  # Loop through columns

        if i == 1 or i == m:  # Print full row on top/bottom
            print(count, end=" ")

        elif j == 1 or j == n :  # Print edges for middle rows
            print(count, end=" ")

        else:  # Print space for inner positions
            print("  ", end="")  # Two spaces for alignment

        count += 1  # Increment count for next column

    print()  # Move to next line after each row
