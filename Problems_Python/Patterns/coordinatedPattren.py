# Taught On Approach
n = int(input())                # Read an integer input from the user
count = 0                       # Initialize a counter to track valid (a, b) pairs

for i in range(1, n + 1):       # Loop through values of a from 1 to n
    a = i                       # Assign current value of a
    for j in range(1, n - i):   # Loop for j such that b = a + j is less than n
        b = a + j               # Compute b as a + j
        if a + b == n:          # Check if the sum of a and b equals n
            count += 1          # If condition is met, increment count

print(count)                    # Output the final count of valid pairs

# Input = 7
# => a + b = n
# Output = count = 3

# (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
# (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
# (3, 4), (3, 5), (3, 6), (3, 7),
# (4, 5), (4, 6), (4, 7),
# (5, 6), (5, 7),
# (6, 7)

# (1, 6)
# (2, 5)
# (3, 4)