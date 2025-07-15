number = int(input("Enter a number: "))

for i in range(2 , number + 1):
    factors = 0
    for j in range(2 , i):
        if i % j == 0:
            factors += 1
    if factors == 0:
        print(i)
