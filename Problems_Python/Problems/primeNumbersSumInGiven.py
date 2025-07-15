n = int(input("How many numbers : "))
sum = 0

while n > 0:
    s = int(input("Enter number: "))
    count = 0
    for i in range(1, s + 1):
        if s % i == 0:
            count += 1

    if count == 2:  # Prime check
        sum += s

    n -= 1  # Decrease n to avoid infinite loop

print("Sum of prime numbers:", sum)
