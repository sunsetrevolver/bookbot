def wordcount(book_string) :
    word_list = book_string.split()
    return len(word_list)

def char_count(book_string) :
    char_dict = {}
    for char in book_string:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

def report(char_counter) :
    listofdict = []
    for char in char_counter:
        listofdict.append({"char": char, "num": char_counter[char]})
    listofdict.sort(reverse=True, key=sort_on)
    return listofdict

def sort_on(items):
    return items["num"]
