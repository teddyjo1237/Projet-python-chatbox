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
print(tf_scores)
print(idf_scores)
tfidf_matrix = calculate_tfidf_matrix(directory_path)
print(find_tf(tf_scores))
print(find_idf(idf_scores))
print(calculate_tfidf_matrix(directory_path))



# Ask the user to enter a question
question = str(input("Enter your question : "))
print(question_analyze(question))