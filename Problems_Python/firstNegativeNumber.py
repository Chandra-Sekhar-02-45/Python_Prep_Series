# Program to read 'n' numbers and print the first negative number encountered, then stop the loop

n = int(input("Enter how many numbers you want to input: "))       # Read the total number of inputs

for i in range(1, n + 1):                                           # Loop from 1 to n
    m = int(input(f"Enter number {i}: "))                          # Read each number from the user
    if m < 0:                                                      # If the number is negative
        print(m)                                                   # Print the first negative number
        break                                                      # Exit the loop immediately
