n = int(input())                    # Take number of rows as input

for i in range(n):                 # Loop through each row (i = 0 to n-1)
    print(" " * i, end="")         # Print i number of spaces for indentation

    count = 0                      # Initialize count to 0 for each row

    for j in range(n - i):         # Loop to print (n - i) numbers in each row
        count += 1                 # Increment count
        print(count, end=" ")      # Print the current count with a space

    print()                        # Move to next line after finishing the row
