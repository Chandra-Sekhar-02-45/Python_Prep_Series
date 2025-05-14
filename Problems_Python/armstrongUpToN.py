n = int(input("Enter a number: "))

for i in range(1, n + 1 ):
    a = str(i)
    k = len(a)
    temp_sum = 0               # Start fresh for each number
    for digit in a:
        temp_sum += int(digit) ** k
    if temp_sum == i:          # Now check after full sum is computed
        print(i)
