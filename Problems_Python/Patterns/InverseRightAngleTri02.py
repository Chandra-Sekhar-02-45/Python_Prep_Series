n = int(input("Enter the number of rows: "))             # Take input for number of rows

k = int((n * (n + 1)) * 0.5)                             # Calculate total numbers using n(n+1)/2 formula

for i in range(n):                                       # Outer loop for each row
    print(" " * 2 * i, end="")                           # Print leading spaces for right alignment

    for j in range(n - i):                               # Inner loop to print decreasing number of elements
        print(k, end=" ")                                # Print the current value of k
        k -= 1                                           # Decrement k after printing

    print()                                              # Move to the next line after each row
