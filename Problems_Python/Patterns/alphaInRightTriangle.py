# Program to print a right-aligned triangle alphabet pattern of height n

n = int(input("Enter the height of the pattern (n): "))               # Read the height of the pattern
word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                                   # Define the alphabet string

for i in range(1, n + 1):                                             # Loop for each row
    space = " " * 2 * (n - i)                                         # Compute leading spaces for right alignment
    row = ""                                                          # Initialize the row string

    for j in range(i):                                                # Loop to add increasing letters
        row += word[j] + " "                                          # Append letter and space

    print(space + row)                                                # Print the complete row with leading spaces
