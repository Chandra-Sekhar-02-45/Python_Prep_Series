# Program to find the largest proper divisor of a given number

n = int(input("Enter a number: "))              # Take input from the user
largest_divisor = 1                             # Initialize with 1 (default if no other divisor found)

for i in range(1, (n // 2) + 1):                # Loop from 1 to n//2 (proper divisors are < n)
    if n % i == 0:                              # Check if 'i' divides 'n' completely
        largest_divisor = i                     # Update the largest divisor found

print("Largest proper divisor:", largest_divisor)  # Print the result
