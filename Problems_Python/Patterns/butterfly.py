n = int(input())

for i in range( 1 , n + 1):
    sp = " " * 4*(n - i)
    star = "* " * i
    row = star + sp + star
    print(row)

for i in range(  n ) :
    sp = " " * 4 * i
    star = "* " * (n - i)
    row = star + sp + star
    print(row)