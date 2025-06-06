# Program to print decreasing sequences of alphabets from A in each row

n = int(input("Enter the number of rows: "))             # Take input for number of rows
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                    # Define the uppercase alphabet string

for i in range(1, n + 1):                                # Loop from 1 to n (row-wise)
    row = ""                                             # Initialize an empty row string
    for j in range(n - i + 1):                           # Loop to print decreasing characters each row
        row += string[j] + " "                           # Append the j-th character from string
    print(row)                                           # Print the constructed row
