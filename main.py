import os
import math
from functions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
president_names = extract_names(files_names)
associate_names(president_names)

convert_to_lowercase("./speeches", "./cleaned")
remove_punctuation("./cleaned")




directory_path = "./cleaned"
idf_scores = idf(directory_path)
tf_scores = tf(directory_path)
tfidf_matrix = calculate_tfidf_matrix(directory_path)