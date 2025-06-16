n = int(input("Enter n : "))

for i in range(1, n + 1):
    space = (n - i) * " "
    star = "*"
    if i == 1:
        row = space + star
        print(row)
    else:
        m_space = (2 * (i - 1) - 1) * " "
        row = space + star + m_space + star
        print(row)

for i in range(1, n):
    space = i * " "
    star = "*"
    if i == (n - 1):
        row = space + star
        print(row)
    else:
        m_sapce = (2 * (n - i - 1) - 1) * " "
        row = space + star + m_sapce + star
        print(row)
