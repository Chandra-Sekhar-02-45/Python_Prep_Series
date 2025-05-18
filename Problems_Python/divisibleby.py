n = int(input("Enter the number : "))      # Input number
count = 0             # Initialize count

for i in range(1, n + 1):
    divisible = False  # Reset flag for each i

    for j in range(2, 11):
        if i % j == 0:
            divisible = True  # i divisible by j
            break

    if not divisible:
        count += 1      # Increment if no divisor found

print(count)          # Output count
