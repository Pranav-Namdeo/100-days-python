import pandas

data = pandas.read_csv("./day 30/NATO/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    try:
        word = input("Enter a word: ").upper()
        phonetic_list = [nato_dict[letter] for letter in word]
        print(phonetic_list)
    except:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

generate_phonetic()
