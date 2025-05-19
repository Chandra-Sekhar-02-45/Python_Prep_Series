n = int(input())  # Read size of the square pattern

for i in range(1, n + 1):  # Loop through rows from 1 to n
    for j in range(1, n + 1):  # Loop through columns from 1 to n

        if i == 1 or j == 1 or i == n or j == n:
            print(j, end=" ")  # Print column number on the border

        else:
            print("  ", end="")  # Print spaces inside the square

    print()  # Move to the next line after each row
