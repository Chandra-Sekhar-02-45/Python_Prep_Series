n = int(input())
fact = n
sum = 0

for i in range(1 , n ) :
    fact *= (n - i)

for i in str(fact):
    sum += int(i)

print(sum)

