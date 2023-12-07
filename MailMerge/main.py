# TODO: Create a letter using starting_letter.txt

# Put names into a list
with open("./Input/Names/invited_names.txt", "r") as names:
    invited_names = names.read().splitlines()

# replace [names] with each name and save txt
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    contents = letter.read()

for name in invited_names:
    custom_letter = contents.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}_letter.txt", "w") as letter:
        letter.write(str(custom_letter))
