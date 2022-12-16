
vowels = ['a', 'e', 'i', 'o', 'u']
LETTERS = "Discipline beats intelligence"

print('Search vowels in the phrase: "Discipline beats intelligence"')
for letter in LETTERS:
    if letter in(vowels):
        print('the vowel is: ' +letter)