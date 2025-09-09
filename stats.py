def get_num_of_words(file_contents):
    words = file_contents.split()
    num_of_words = len(words)
    return num_of_words


def times_char_appears(book_text):
    chars = list(book_text)
    times_char_appears = {}
    for char in chars:
        char = char.lower()
        if char in times_char_appears:
            times_char_appears[char] += 1
        else:
            times_char_appears[char] = 1
    return times_char_appears