# Program to find the LCM (Least Common Multiple) of two numbers using a simple loop to find GCD

m = int(input("Enter the first number (m): "))                    # Read first number
n = int(input("Enter the second number (n): "))                   # Read second number

num = 1                                                           # Initialize variable to store GCD

for i in range(1, min(m, n) + 1):                                 # Loop from 1 to min(m, n)
    if m % i == 0 and n % i == 0:                                 # Check if i divides both m and n
        num = i                                                   # Update GCD if i is a common divisor

lcm = (m * n) // num                                              # Calculate LCM using (m * n) // GCD

print("LCM of", m, "and", n, "is:", lcm)                          # Print the LCM
