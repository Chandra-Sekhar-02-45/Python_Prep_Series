n = int(input())
count = 1

for i in range(1 , n + 1) :
    if i == 1 :
        for j in range(1 , n + 1) :
            print(count , end = " ")
            count += 1
        print()
    elif i == n :
        row = " " * (n - 1)
        print(row + "1 ")
    else :
        sp = " " * (i - 1)
        h_sp = " " * 2*(n - i - 1)
        num = n - i + 1
        row = sp + "1 " + h_sp + str(num)
        print(row)