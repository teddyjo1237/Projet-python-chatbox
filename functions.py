'''
- Extract the names of the presidents from the names of the text files provided ;
def extract_name:

- Associate a first name with each president;
- Display the list of president's names (watch out for duplicates) ;
- Convert the texts in the 8 files to lower case and store the contents in new files. The new files are to be
stored in a new folder called "cleaned". This folder should be located in the main directory of the main.py
program, and at the same level as the "speeches" directory.
- For each file stored in the "cleaned" directory, run through its text and remove any punctuation characters.
The final result should be a file with words separated by spaces. Please note that some characters, such as
the apostrophe (') or the dash (-), requires special treatment to avoid concatenating two words (e.g. "ellemême" should become "elle même" and not "ellemême"). Changes made at this phase should be stored
in the same files in the "cleaned" directory.'''


import os

# Run through the list of files
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def print_list(list_name):
    print(list_name)

def list_of_names(name_file):
    names_list = []
    last_name = "test"
    for i in range(len(name_file)):
        name_without_nbr = "".join([j for j in name_file[i] if not j.isdigit()])
        name = name_without_nbr.replace("Nomination_","")
        name = name.replace(".txt","")
        if name != last_name:
            names_list.append(name)
        last_name = name
    return names_list