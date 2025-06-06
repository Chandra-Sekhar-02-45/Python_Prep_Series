# Program to print the digit '6' using stars (*) in a pattern of size n

n = int(input("Enter the value of n: "))              # Input size of the digit

for i in range(1, n):                                  # Loop from 1 to n-1 for top part
    if i == 1:                                         # For first line
        star = "* " * n                                # Print n stars for top horizontal line
        print(star)                                    # Output the stars
    else:
        for j in range(1, n):                          # Loop from 1 to n-1 for printing star column
            if j == 1:                                 # If first column
                print("* ", end=" ")                   # Print star with space
        print()                                        # Move to next line

for i in range(1, n + 1):                              # Loop for bottom block rows
    for j in range(1, n + 1):                          # Loop for columns
        if i == 1 or i == n or j == 1 or j == n:     # Stars at first/last row or first/last column
            print("*", end=" ")                        # Print star with space
        else:
            print(" ", end=" ")                        # Print space inside hollow area
    print()                                            # New line after each row
