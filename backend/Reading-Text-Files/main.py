# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    file = open(filename, 'r')
    file_content = file.read()

    # removing punctuations from the string
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in file_content:
        if ele in punc:
            file_content = file_content.replace(ele, "")
    yield file_content
    # return file_content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    file_content = (next(text)).split()

    word_counts = {word: file_content.count(word) for word in file_content}
    return word_counts


print(count_words())
