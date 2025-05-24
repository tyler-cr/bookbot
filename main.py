from stats import *
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        bookfile = sys.argv[1]

    char_count = get_num_chars(bookfile)
    word_count = get_num_words(bookfile)

    sorted_list = get_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(f"{dict["name"]}: {dict["num"]}")
    print("============= END ===============")

main()