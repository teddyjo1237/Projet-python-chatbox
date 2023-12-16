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

def calculate_tfidf_matrix(directory):
    tfidf_matrix = []
    unique_words = set()
    document_frequency = {}
    total_documents = 0

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            total_documents += 1
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().lower().split()
                unique_words.update(set(content))

                for word in set(content):
                    document_frequency[word] = document_frequency.get(word, 0) + 1

    for filename in os.listdir(directory):      # Calculating the TF-IDF of each word in each document
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().lower().split()

                tf_vector = {word: content.count(word) / len(content) for word in set(content)}

                # Calculating TF-IDF
                tfidf_vector = [tf_vector[word] * math.log(total_documents / document_frequency[word], 10) if word in tf_vector and document_frequency[word] > 0 else 0 for word in unique_words]

                tfidf_matrix.append(tfidf_vector)

    return tfidf_matrix

# I didn't have time to call functions in other functions so I just put them manually in the TF-IDF function for now

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


# Part II
<<<<<<< HEAD
=======

def question_analyze(question):
    words_question = []
    question_lower = question.lower()
    punctuation = """!#$%&()*"+,./:;<=>?@[\]^_`{|}~"""
    question_cleaned = question_lower.translate(str.maketrans("'", " ", "")).translate(str.maketrans("-", " ", "")).translate(str.maketrans("", "",punctuation))
    for word in question_cleaned:
        words_question.append(word)
    return words_question

'''Write a function that identifies the terms in the question that are also present in the document
corpus. Ignore terms absent from the corpus, as they will have no associated TF-IDF values. In other
words, look for terms that form the intersection between the set of words in the corpus and the
set of words in the question.'''
#!!!!!!!!!!!!!!!!!!!!!!! a modifier pour inclure (version prototype): Mon test pour verifier si les mots d'une questions sont dans un doc texte, retourne une liste avec les mots qui y sont.
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


question_set = check_existance(list_of_file,list_of_question)
print(question_set)'''




# Part 3
#removing apostrophe neads to be imporved!!!!!!!!!!
'''def clean_up(string):
    i=0
    newstr = ""
    for i in range(len(string)):

        if string[i] == "'":
            newstr += "e "
        else:
            newstr+=string[i]
    return(newstr)'''
>>>>>>> 36e3856d97475d63acdfef25628768124e2409c8
