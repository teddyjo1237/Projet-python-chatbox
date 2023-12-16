# Question entered by the user

def question_analyze(question):
    words_question = []
    word = ""
    question_lower = question.lower()
    punctuation = """!#$%&()*"+,./:;<=>?@[\]^_`{|}~"""
    question_cleaned = question_lower.translate(str.maketrans("'", " ", "")).translate(str.maketrans("-", " ", "")).translate(str.maketrans("", "",punctuation))
    for char in question_cleaned:
        if char != " ":
            word = word + char
        elif char == " " and word != "":
            words_question.append(word)
            word = ""

    if word != " " and word != "":
        words_question.append(word)
    return words_question