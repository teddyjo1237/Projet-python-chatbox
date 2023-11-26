import os
from functions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)
president_names = extract_names(files_names)
print_list(president_names)
print(associate_names(president_names))

convert_to_lowercase("./speeches", "./cleaned")
remove_punctuation("./cleaned")

test = "hello hello this is a string test to see if our code work "
print(tf(test))