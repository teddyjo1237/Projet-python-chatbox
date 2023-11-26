import os


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
        
        with open(input_filepath, "r")  as file:
            content = file.read()
        content_lower = content.lower()
        with open(output_filepath, "w") as file:
            file.write(content_lower)


def remove_punctuation(input_folder):
    input_folder_path = os.path.join(os.getcwd(), input_folder)
    for filename in os.listdir(input_folder_path):
        input_filepath = os.path.join(input_folder_path, filename)   # Create the path to the files

        with open(input_filepath, "r") as file:
            content = file.read()
        punctuation = """!#$%&()*"+,./:;<=>?@[\]^_`{|}~"""
        remove_apostrophe = str.maketrans("'", " ", "")    # Remove punctuation characters and handle special cases
        remove_dash = str.maketrans("-", " ", "")    
        remover = str.maketrans("", "",punctuation) 
        content_cleaned = content.translate(remove_apostrophe).translate(remove_dash).translate(remover)
        with open(input_filepath, "w") as file:
            file.write(content_cleaned)


# Create a string from a speech file
def create_str():
    t = 1

# TF method
def tf(string):
    dict = {}
    found = False
    keys = []

    word = ""
    for chr in string:
        if chr != " ":
            word = word + chr
        elif chr == " ":
            keys.append(word)
            word = ""
    if word != "":
        keys.append(word)

    for i in range(len(keys)):
        current_word = keys[i]
        for key in dict:
            if current_word == key:
                dict[current_word] += 1
                found = True
        if not(found):
            dict[current_word] = 1
        found = False



    return keys, dict