import pandas

# TODO 1. Create a dictionary.
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    word = input("What word do you want coded in the NATO alphabet?: ").upper()
    try:
        coded_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters from the alphabet please.")
        generate_phonetic()
    else:
        print(coded_word)

generate_phonetic()
