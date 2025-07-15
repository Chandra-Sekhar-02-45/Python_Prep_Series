n = int(input())

while n > 0 :
    m = int(input())

    for i in range( 2 , m ):
        count = 0
        if m % i == 0 :
            count += 1
            if count == 0 :
                print(m)
                break

    n -= 1














