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

def sort_on(items):
    return items["num"]

# Turn dictionary into sorted list of dictionaries
def sort_dict(dict):

    sorted_list = []

    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list