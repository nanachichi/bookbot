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


def sort_on(items):
    return items["num"]


def sort_times_char_appears(char_count):
    list_char_count = []
    for key, value in char_count.items():
        char_times = {"char": key, "num": value}
        list_char_count.append(char_times)

    list_char_count.sort(reverse=True, key=sort_on)
    return list_char_count