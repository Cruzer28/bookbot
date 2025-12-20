from stats import get_word_count

def get_book_text(file):
    with open(file) as f:    
        file_contents = f.read()
        return file_contents
    

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)

    print(f"Found {word_count} total words")


main()
