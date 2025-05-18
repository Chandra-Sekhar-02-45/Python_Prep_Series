n = int(input("Enter the ending number (n): "))          # Input the last number of the pattern
k = int(input("Enter the number of rows (k): "))         # Input number of rows in the triangle

count = n + (k * (k + 1)) // 2                           # Calculate starting number before the first row

for i in range(k):                                       # Loop for each row
    for j in range(i + 1):                               # Loop for each element in the row
        count -= 1                                       # Decrease count to print in reverse
        print(count, end=" ")                            # Print the current number
    print()                                              # Move to next line after each row
