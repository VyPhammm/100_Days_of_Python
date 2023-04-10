import pandas as pd

nato = pd.read_csv(r"Day26_Dict-Comprehension\nato_phonetic_alphabet.csv")

nato_list = {row.letter:row.code for (index, row) in nato.iterrows()}

def generate_phonetic():
    code_words = input("Enter a word: ").upper()
    try:
        result = [nato_list[code] for code in code_words]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generate_phonetic()
    else:
        print(result)
generate_phonetic()