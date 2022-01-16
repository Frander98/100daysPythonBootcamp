import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

word_to_spell = input("Enter a word: \n").upper()

# Option 1 using dict comprehension
letter_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Option 2 using normal for loop
# letter_dict = {}
# for (index, row) in df.iterrows():
#     letter_dict[row.letter] = row.code

ask = True
while ask:
    try:
        phonetic_letter_list = [letter_dict[letter] for letter in word_to_spell]
    except KeyError:
        print("Only letters in the Alphabet, please.")
        word_to_spell = input("Enter a word: \n").upper()
    else:
        print(phonetic_letter_list)
        ask = False
