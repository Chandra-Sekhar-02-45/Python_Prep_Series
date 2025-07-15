# Prime Numbers:
# A prime number is a natural number greater than 1 that has only two distinct positive divisors: 1 & Itself.

# Taught On Approach:

n = int(input("Enter the upper limit: "))   # Input the upper limit

for i in range(2, n + 1):                   # Loop through each number from 2 to n
    count = 0                               # Counter to track how many numbers divide 'i'

    for j in range(2, i):                   # Check if 'i' is divisible by any number from 2 to i-1
        if i % j == 0:
            count += 1                      # Found a divisor

    if count == 0:                          # If no divisors were found, then 'i' is prime
        print(i)
