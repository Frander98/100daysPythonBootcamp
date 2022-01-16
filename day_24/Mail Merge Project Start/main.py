
with open("./Input/Letters/starting_letter.txt", "r+") as letter_file:
    letter = letter_file.read()

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

for name in names:
    formated_name = name.strip()
    new_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{formated_name}", "w") as final_letter:
        final_letter.write(new_letter)




