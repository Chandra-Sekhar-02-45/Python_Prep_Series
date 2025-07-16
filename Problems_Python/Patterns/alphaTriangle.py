# Program to print an alphabet triangle pattern of height n

n = int(input("Enter the height of the triangle (n): "))       # Read the height of the triangle
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                               # Define the uppercase alphabet string

for i in range(1, n + 1):                                      # Loop for each row
    row = ""                                                    # Initialize the row string
    for j in range(0, i):                                       # Loop to add letters up to i
        row += a[j] + " "                                       # Append the letter and space
    print(row)                                                  # Print the completed row
