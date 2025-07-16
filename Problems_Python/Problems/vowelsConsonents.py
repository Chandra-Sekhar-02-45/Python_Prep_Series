# Program to count the number of vowels and consonants in a given string

word = input("Enter a string: ")                               # Read the input string
vow = "AEIOUaeiou"                                             # Define all vowels (both cases)
length = len(word)                                             # Get the total length of input
countVow = 0                                                    # Initialize vowel count

for i in word:                                                  # Loop through each character
    if i == " " or i == ".":                                    # Ignore spaces and periods
        length -= 1                                             # Reduce total letter count
    for j in vow:                                               # Check for vowels
        if i == j:
            countVow += 1                                       # Increment vowel count

print("Vowels:", countVow)                                      # Print number of vowels
print("Consonants:", length - countVow)                         # Print number of consonants
