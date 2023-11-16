'''Extract the names of the presidents from the names of the text files provided ;
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


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
