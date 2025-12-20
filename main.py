def get_book_text(file):
    with open(file) as f:    
        file_contents = f.read()
        return file_contents
    
def get_word_count(text):
    word_count = 0
    words = text.split()

    for word in words:
        word_count +=1

    return word_count

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)

    print(f"Found {word_count} total words")


main()
