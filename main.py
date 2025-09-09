def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def get_num_of_words(file_contents):
    words = file_contents.split()
    num_of_words = len(words)
    return num_of_words
