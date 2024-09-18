#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#dictionary_letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_book_words(text)
    letters = get_book_letters(text)
    sortedLetters = get_sorted_char(letters)
    #print(text)
    print(f"word length: {words}")
    for c in sortedLetters:
        print(f"The '{c}' character was found {sortedLetters[c]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_words(text):
    return len(text.split())

def get_book_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_char(letters):
    mykeys = list(letters.keys())
    for c in mykeys:
        if c.isalpha() == False:
            del letters[c]
    mykeys = list(letters.keys())
    mykeys.sort()
    return {i: letters[i] for i in mykeys}


# def get_book_letters(text):
#     letterString = []
#     lowerString = text.lower()
#     for let in lowerString:
#         letterString.append(let)
#     for x in letters:
#         for y in letterString:
#             if x == y:
#                 count = dictionary_letters[x]
#                 count += 1
#                 dictionary_letters[x] = count
#     return dictionary_letters




#     chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

#     print(f"--- Begin report of {book_path} ---")
#     print(f"{num_words} words found in the document")
#     print()

#     for item in chars_sorted_list:
#         if not item["char"].isalpha():
#             continue
#         print(f"The '{item['char']}' character was found {item['num']} times")

#     print("--- End report ---")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def sort_on(d):
#     return d["num"]


# def chars_dict_to_sorted_list(num_chars_dict):
#     sorted_list = []
#     for ch in num_chars_dict:
#         sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
#     sorted_list.sort(reverse=True, key=sort_on)
#     return sorted_list

main()






#Full from class code:
# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     chars_dict = get_chars_dict(text)
#     chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

#     print(f"--- Begin report of {book_path} ---")
#     print(f"{num_words} words found in the document")
#     print()

#     for item in chars_sorted_list:
#         if not item["char"].isalpha():
#             continue
#         print(f"The '{item['char']}' character was found {item['num']} times")

#     print("--- End report ---")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def sort_on(d):
#     return d["num"]


# def chars_dict_to_sorted_list(num_chars_dict):
#     sorted_list = []
#     for ch in num_chars_dict:
#         sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
#     sorted_list.sort(reverse=True, key=sort_on)
#     return sorted_list


# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()