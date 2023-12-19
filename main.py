import os
import math
from functions import *
from question import *

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
tfidf_matrix = tf_idf_matrix(directory_path)
unimportant = unimportant_words(directory_path)


# Menu

choice = 1000
while choice != 0:
    print("[0]---Leave")
    print("[1]---Print the unimportant words")
    print("[2]---Print tf matrix")
    print("[3]---Print idf matrix")
    print("[4]---Print td-idf matrix")
    print("[5]---Ask a question")
    choice = int(input("Enter your choice ---> "))
    if choice == 1:
        print(unimportant)
    elif choice == 2:
        print(tf_scores)
    elif choice == 3:
        print(idf_scores)
    elif choice == 4:
        print(tfidf_matrix)
    elif choice == 5:
        # Ask the user to enter a question
        question = str(input("Enter your question : "))
        print(question_analyze(question))   