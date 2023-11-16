import os
from functions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)