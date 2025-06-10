s = input()
count = 0
word = ""

for i in s:
    if i == " ":
        break
    else:
        word += i.upper()
        count += 1

word += s[count:]
print(word)