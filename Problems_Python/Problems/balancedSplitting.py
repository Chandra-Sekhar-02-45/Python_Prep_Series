# Problem: Count how many balanced substrings are in the given word
# A balanced substring has an equal number of 'L' and 'R' characters.

word = input("Enter a string of 'L' and 'R' only: ")  # For example: LRLRRLLR

balance = 0  # Tracks the net difference between L and R
count = 0    # Counts the number of balanced parts

for char in word:
    if char == 'L':
        balance += 1   # L increases balance
    else:
        balance -= 1   # R decreases balance

    if balance == 0:   # If balance becomes 0, it means equal Ls and Rs so far
        count += 1     # One balanced substring found

print(f"Number of balanced substrings: {count}")
