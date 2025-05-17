n = int(input())               # Read number of rows from the user

for i in range(1, n + 1):      # Loop through each row
    count = 1                  # Initialize count for the first part
    m = 1                      # Initialize m for the second part

    for j in range(1, i + 1):  # Print increasing numbers from 1 to i
        print(count, end=" ")
        count += 1

    for k in range(1, i):      # Print increasing numbers from 1 to i-1
        print(m, end=" ")
        m += 1

    print()                     # Move to the next line after each row
