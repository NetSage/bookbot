from stats import get_num_words
from stats import get_num_chars
from stats import chars_dict_to_sorted_list
import sys


def get_book_text(filepath):
    with open(filepath) as text:
        return text.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_location = sys.argv[1]
    book_text = get_book_text(book_location)

    words = get_num_words(book_text)
    characters = get_num_chars(book_text)

    char_sorted_list = chars_dict_to_sorted_list(characters)

    print("============ BOOKBOT ============")
    print(f"Anaylzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
