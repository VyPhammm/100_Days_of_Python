#  Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"

with open(r"Day24_Mail-Merge\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    list_name = names_file.readlines() 

with open(r"Day24_Mail-Merge\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in list_name:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Day24_Mail-Merge\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode="w") as mail:
            mail.write(new_letter)