from stats import get_word_count, get_character_count

def get_book_text(file):
    with open(file) as f:    
        file_contents = f.read()
        return file_contents
    

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    character_count = get_character_count(text)

    print(f"Found {word_count} total words")

    for char in character_count:
        number = character_count[char]
        print(f"'{char}': {number}")


main()
