import sys
from stats import get_word_count, get_character_count, sort_dict

# Retrieve text file and return contents
def get_book_text(file):
    with open(file) as f:    
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    word_count = get_word_count(text)
    unsorted_character_count = get_character_count(text)
    character_count = sort_dict(unsorted_character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    # Print out list and number of each character from text
    for line in character_count:
        char = line["char"]
        num = line["num"]

        # Include only alphabetical characters
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")


main()
