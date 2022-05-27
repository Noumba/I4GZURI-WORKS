# reading the input text
given_text = input("Enter text here: ")

# function that count words in given text


def word_count(text):
    word_count = text.split(" ")
    print("Total number of words is: " + str(len(word_count)))
    return len(word_count)


word_count(given_text)
