# Program to print the first n uppercase alphabets repeated in each of n rows

n = int(input("Enter the number of rows: "))           # Take input for number of rows
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                  # Define the uppercase alphabet string

for i in range(1, n + 1):                              # Loop through rows 1 to n
    row = ""                                           # Initialize empty string for each row
    for j in range(n):                                 # Loop to print n characters in each row
        row += string[j] + " "                         # Append j-th character with a space
    print(row)                                         # Print the constructed row
