import pandas as pd

nato = pd.read_csv(r"Day26_Dict-Comprehension\nato_phonetic_alphabet.csv")

nato_list = {row.letter:row.code for (index, row) in nato.iterrows()}

code_words = input("Enter a word: ").upper()

result = [nato_list[code] for code in code_words]
print(result)