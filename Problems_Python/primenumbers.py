number = int(input())

for i in range(2 , number + 1) :
    factors = 0
    for j in range(2 , i ) :
        if number % j == 0 :
            factors += 1
    if factors == 0 :
        print(i)
