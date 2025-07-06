from stats import wordcount
from stats import char_count
from stats import report
import sys

def get_book_text(file_path) :

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main ():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    bookfile = sys.argv[1]
    local_dict = char_count(get_book_text(bookfile))
    sorted_list = report(local_dict)
    count = wordcount(get_book_text(bookfile))
    for key in local_dict:
        print(f'\'{key}\' : {local_dict[key]}')
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {count} total words')
    print('--------- Character Count -------')
    for item in sorted_list:
        if item['char'].isalpha() :
            print(f'{item['char']}: {item['num']}') 
    print('============= END ===============')
main()
