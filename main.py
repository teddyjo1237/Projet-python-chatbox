import os
from functions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
president_names = list_of_names(files_names)
print_list(president_names)