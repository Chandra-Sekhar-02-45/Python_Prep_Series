#Composite numbers are positive integers greater than 1 that have more than
# two positive divisors — in other words, numbers that are not prime.

#Taught On Approach :
m = int(input())    # Input: start of the range (integer)
n = int(input())    # Input: end of the range (integer)

for i in range(m, n + 1):    # Iterate through all numbers from m to n
    count = 0                # Initialize divisor count for current number i

    for j in range(1, i + 1):  # Check all numbers from 1 to i to find divisors
        if i % j == 0:
            count += 1        # Increment count if j is a divisor of i

    if count > 2:             # If number has more than 2 divisors, it is not prime
        print(i)              # Print the number
