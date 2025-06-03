n = int(input("Number Of Inputs : "))

while (n > 0):
    m = input("Enter a number : ")
    length = len(m)
    arm = 0
    for i in m:
        arm += int(i) ** length

    if int(m) == arm:
        print(m)
    n -= 1


