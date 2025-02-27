def get_num_words(file_content):
    str_arr = file_content.split()
    word_count = len(str_arr)
    
    print(f"Found {word_count} total words")

def get_character_dict(file_content):
    str_dict = {}
    
    for character in file_content:    

        if not character.isalpha():
            continue
        
        compare_char = character.lower()
 
        if compare_char in str_dict:
            str_dict[compare_char] += 1
        else:
            str_dict[compare_char] = 1

    return str_dict

def sort_on(tuple):
    return tuple[1]

def sort_to_tuple(dictionary):
    arr = []
    for entry in dictionary:
        arr.append((entry,dictionary[entry]))

    arr.sort(reverse=True, key=sort_on)

    return arr