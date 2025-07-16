# Program to print a symmetric numeric pyramid pattern of height n

n = int(input("Enter the height of the pyramid (n): "))         # Read the height of the pyramid
row = ""                                                        # Initialize row string

for i in range(1, n + 1):                                       # Loop for each row
    first = 1                                                    # Initialize ascending number
    second = i - 1                                               # Initialize descending number

    for j in range(1, i + 1):                                    # Loop to print ascending numbers
        print(first, end="")                                     # Print ascending number
        first += 1                                               # Increment ascending number

    for k in range(1, i):                                        # Loop to print descending numbers
        print(second, end="")                                    # Print descending number
        second -= 1                                              # Decrement descending number

    print()                                                      # Move to next line after each row
