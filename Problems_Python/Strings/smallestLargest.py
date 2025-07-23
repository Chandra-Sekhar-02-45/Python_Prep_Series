# 🔍 Find the Lexicographically Smallest and Largest Words in a Sentence

# Take the input string from the user
s = input("Enter a sentence: ")  # Example: Apple mango Zebra Ball cherry

first = "z"  # Initialize to a very large word (lexicographically)
last = ""          # Initialize to an empty word
row = ""           # To hold characters of the current word

# Loop through each character in the string
for i in range(len(s)):
    char = s[i]  # Get the current character

    if char != " ":  # If not a space, build the current word
        row += char

    # If we reach a space or the end of the string, it's end of a word
    if char == " " or i == len(s) - 1:
        if row:  # Make sure it's not empty
            if row.lower() < first.lower():  # Compare with smallest so far
                first = row

            if row.lower() > last.lower():  # Compare with largest so far
                last = row

            row = ""  # Reset to process the next word

# Print the result
print("\nFinal Result:")
print("Smallest word (lexicographically):", first)
print("Largest word (lexicographically):", last)
