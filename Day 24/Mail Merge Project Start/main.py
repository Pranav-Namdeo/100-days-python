#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./day 24/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names =  names_file.readlines()

with open("./day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as Letter_file:
    letter = Letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./day 24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)