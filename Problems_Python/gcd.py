m = int(input())
n = int(input())
max_num = 0

if m > n :
    ind = n
else:
    ind = m

if m == 0 : print(n)
elif n == 0 : print(m)
else :
    for i in range(1, ind + 1):
        num = 0
        if m % i == 0 and n % i == 0:
            if i > num :
                num = i
                if num > max_num :
                    max_num = num
    print(max_num)












