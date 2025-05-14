n = int(input())

for i in range(n) :
    print(" " * 2*(n - i - 1) , end = "")
    k = i + 1
    for j in range(i + 1) :
        print(k , end = " ")
        k -= 1
    print()

#Single Loop
# n = int(input())
#
# for i in range(n):
#     row = " " * (2 * (n - i - 1))
#     print(row + "* " * (i + 1))