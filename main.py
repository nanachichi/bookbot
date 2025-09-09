from stats import get_num_of_words, times_char_appears, sort_times_char_appears
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

        book_text = get_book_text(filepath)
        word_count = get_num_of_words(book_text)
        char_count = times_char_appears(book_text)
        list_char_appears = sort_times_char_appears(char_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for dictionary in list_char_appears:
            if dictionary["char"].isalpha():
                count = f'{dictionary["char"]}: {dictionary["num"]}'
                print(count)
        print("============= END ===============")


main()