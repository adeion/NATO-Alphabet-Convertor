import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
data = pandas.DataFrame(df)
new_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}
print(new_dict)
while True:
    try:
        User_word = input("Enter a word for Translation: ").upper()
        user_list = [new_dict[letter] for letter in User_word]
    except KeyError:
        print('We only accept words not numbers please try again')
    finally:
        print(user_list)
        