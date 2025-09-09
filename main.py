from stats import get_num_of_words, times_char_appears


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_of_words(book_text)
    char_count = times_char_appears(book_text)
    print(word_count)
    print(char_count)


main()