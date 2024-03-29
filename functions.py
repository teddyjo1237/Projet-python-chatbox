import os
import math

# Run through the list of files
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Allow to print in form of a list
def print_list(list_name):
    for i in range(len(list_name)):
        print(list_name[i])


# Remove extensions and keep only the name of the presidents
def extract_names(name_file):
    names_list = []
    last_name = "test"
    for i in range(len(name_file)):
        name_without_nbr = "".join([j for j in name_file[i] if not j.isdigit()])
        name = name_without_nbr.replace("Nomination_","")
        name = name.replace(".txt","")
        if name != last_name: # To avoid having twice the same name
            names_list.append(name)
        last_name = name
    return names_list

# Associate each president name with its first name and store it in a dictionary
def associate_names(name_list):
    names_dict = {}
    first_names = ["Jacques", "Valerie", "Francois", "Emmanuel", "Francois", "Nicolas"]
    i = 0
    for names in name_list:
        names_dict[names] = first_names[i]
        i += 1
    return names_dict



def convert_to_lowercase(input_folder, output_folder):
    cleaned_folder = os.path.join(os.getcwd(), output_folder)
    os.makedirs(cleaned_folder, exist_ok=True)     # Create a new cleaned folder

    input_folder_path = os.path.join(os.getcwd(), input_folder)
    for filename in os.listdir(input_folder_path):
        input_filepath = os.path.join(input_folder_path, filename)   # Create the path to the files
        output_filepath = os.path.join(cleaned_folder, filename)
        
        with open(input_filepath, "r", encoding='utf-8')  as file:
            content = file.read()
        content_lower = content.lower()
        with open(output_filepath, "w", encoding='utf-8') as file:
            file.write(content_lower)


def remove_punctuation(input_folder):
    input_folder_path = os.path.join(os.getcwd(), input_folder)
    for filename in os.listdir(input_folder_path):
        input_filepath = os.path.join(input_folder_path, filename)   # Create the path to the files

        with open(input_filepath, "r", encoding='utf-8') as file:
            content = file.read()
        punctuation = """!#$%&()*"+,./:;<=>?@[\]^_`{|}~"""
        remove_apostrophe = str.maketrans("'", " ", "")    # Remove punctuation characters and handle special cases
        remove_dash = str.maketrans("-", " ", "")    
        remover = str.maketrans("", "",punctuation) 
        content_cleaned = content.translate(remove_apostrophe).translate(remove_dash).translate(remover)
        with open(input_filepath, "w", encoding='utf-8') as file:
            file.write(content_cleaned)

def tf(directory):
    doc_frequency = {}

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            unique_words = set() # To be sure that each word is different

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().split()

                for word in set(content):       # Count the frequency of each word in the current document
                    unique_words.add(word)
                    doc_frequency[word] = doc_frequency.get(word, 0) + 0

                for word in content:       # Updating the document frequency
                    doc_frequency[word] = doc_frequency.get(word, 0) + 1
    return doc_frequency


def idf(directory):
    doc_frequency = {}
    total_documents = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            total_documents += 1

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().split()

                for word in set(content):       # Count the frequency of each word in the current document
                    doc_frequency[word] = doc_frequency.get(word, 0) + 1

    idf_scores = {}
    for word, doc_freq in doc_frequency.items():    # Calculating IDF for each word
        idf_scores[word] = math.log(total_documents / doc_freq, 10)

    return idf_scores

def transpose(matrix):
    # Calculate the transpose of a matrix
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def tf_idf_matrix(directory):
    # Calculate TF-IDF matrix
    doc_frequency = tf(directory)
    idf_scores = idf(directory)

    unique_words = list(doc_frequency.keys())
    tf_idf_matrix = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().split()
                tf_scores = [content.count(word) for word in unique_words]
                tf_idf_row = [tf * idf_scores[word] for tf, word in zip(tf_scores, unique_words)]
                tf_idf_matrix.append(tf_idf_row)

    # Transpose the matrix
    tf_idf_matrix = transpose(tf_idf_matrix)

    return tf_idf_matrix, unique_words

# Find a word in the tf-scores
def find_tf(tf_scores):
    user_word = str(input("Enter a word: "))
    user_word_tf = tf_scores[user_word]
    return user_word_tf

# Find a word in the idf-scores
def find_idf(idf_scores):
    user_word = str(input("Enter a word: "))
    user_word_idf = idf_scores[user_word]
    return user_word_idf

def unimportant_words(directory):
    matrix = tf_idf_matrix(directory)
    unimportant_word = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0][i])):
            if matrix[0][i] != 0:
                unimportant = False
        if unimportant == True:
            unimportant_word.append(matrix[1][i])
        unimportant = True
    return unimportant_word

# Part II


#from here the functions work on their own but not in the main program
'''file = open("texte.txt", "r")
data = file.read()
list_of_file = data.replace('\n', ' ').split(" ")
print(list_of_file)
question = str(input("Enter a question"))
list_of_question = question.split(" ")
print(list_of_question)
def check_existance(file,question) :
    questionlist = []
    i=0
    j=0
    for i in range(len(question)):
        for j in range(len(file)):
            if question[i] == file[j]:
                questionlist.append(question[i])
    question_set = set(questionlist)
    return (questionset)




def starters(list_question):
    if list_question[0] == "Comment" :
        start_answer = "Après analyse, "
    elif list_question[0] == "Pourquoi" :
        start_answer = "Après analyse, "
    elif list_question[0] == "Peux-tu" :
        start_answer = "Oui, bien sûr!"
    else:
        start_answer = ""
    return start_answer

def most_relevant(TF_IDF_matrix,tf_question,list_file_names):
    for file in directory:
        average_file = abs(file_tf - question_tf)
        if average_file < current_file_tf :
            current_file_tf = average_file


def clean_up(string):
    i=0
    newstr = ""
    for i in range(len(string)):

        if string[i] == "'":
            newstr += "e "
        else:
            newstr+=string[i]
    return(newstr)

def check_existance(file,question) :
    questionlist = []
    i=0
    j=0
    for i in range(len(question)):
        for j in range(len(file)):
            if question[i] == file[j]:
                questionlist.append(question[i])
    question_set = set(questionlist)
    return (question_set)



def dot_product(tf_idf_question, tf_idf_file):
   return sum(tf_idf_question[i]*tf_idf_file[i] for x_i, y_i in zip(x, y))

def dot_product(matrix1, matrix2):
   if len(matrix1[0]) != len(matrix2):
        raise ValueError("Incompatible matrix dimensions for dot product")

    result_rows = len(matrix1)
    result_cols = len(matrix2[0])

    result_matrix = [[0 for _ in range(result_cols)] for _ in range(result_rows)]

    for i in range(result_rows):
        for j in range(result_cols):
            result_matrix[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0])))

    return result_matrix

def vector_magnitude(vector):
    sum_of_squares = sum(x**2 for x in vector)

    magnitude = math.sqrt(sum_of_squares)

    return magnitude
    
def similarity(vector_A,vector_B):
    denominateur = vector_magnitude(vector_A)*vector_magnitude(vector_B)
    numerator = dot_product(vector_A,vector_B)
    coeficient = numerator/denominateur
    return coeficient


def starters(list_question):
    if list_question[0] == "Comment" :
        start_answer = "Après analyse, "
    elif list_question[0] == "Pourquoi" :
        start_answer = "Après analyse, "
    elif list_question[0] == "Peux-tu" :
        start_answer = "Oui, bien sûr!"
    else:
        start_answer = ""
    return start_answer

def most_relevant(TF_IDF_matrix,tf_question,list_file_names):
    for file in directory:
        average_file = abs(file_tf - question_tf)
        if average_file < current_file_tf :
            current_file_tf = average_file
    
    return name_file_most_similar

def highest_IDF():

    return answer

# Part 3
#removing apostrophe neads to be imporved!
def clean_up(string):
    i=0
    newstr = ""
    for i in range(len(string)):

        if string[i] == "'":
            newstr += "e "
        else:
            newstr+=string[i]
    return(newstr)'''
