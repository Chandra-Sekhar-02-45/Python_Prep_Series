s = int(input())
n = int(input())

for i in range(1 , n + 1) :
    if i == 1:
        for j in range(1 , n + 1) :
            print(s , end = " ")
            s += 1
        print()
    elif i == n :
        sp = " " * (i - 1)
        print(sp + str(s))
    else :
        sp = " " * (i - 1)
        num1 = str(s)
        hsp = 2*(n - i)
        h_sp = " " * (2*(n - i) - 1)
        num2 = str(s + n - i)
        row = sp + num1 + h_sp + num2
        print(row)
        s = int(num2) + 1