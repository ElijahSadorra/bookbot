import os, sys
from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
    raise Exception("File error")

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_books>") 
        sys.exit(1)
    
    file_path = f"{os.getcwd()}/{sys.argv[1]}"

    file_content = get_book_text(file_path)
    print(get_num_words(file_content))

    char_dict = get_character_dict(file_content)
    tuple_arr = sort_to_tuple(char_dict)

    for i in range(len(tuple_arr)):
        letter, count = tuple_arr[i]
        print(f"{letter}: {count}")


main()