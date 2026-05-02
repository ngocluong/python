student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

list_data = {}
import pandas
from pathlib import Path

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / 'nato_phonetic_alphabet.csv'
df = pandas.read_csv(csv_path)
new_list = { row.letter: row.code for (index, row) in df.iterrows()}
print(new_list)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
enter = True
while enter:
    given_name = input("Enter the Name: ")
    try:
        output = { word:new_list[word.upper()] for word in list(given_name.replace(' ', ''))}
    except KeyError:
        print("incorrect name")
    else:
        print(output)
        enter = False