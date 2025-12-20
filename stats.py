def get_word_count(text):
    word_count = 0
    words = text.split()

    for word in words:
        word_count +=1

    return word_count

def get_character_count(text):
    character_count = {}
    text = text.lower()
    chars = list(text)

    for char in chars:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] +=1
    
    return character_count