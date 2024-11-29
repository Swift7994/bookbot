def main():
    book_path = get_book_path()
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    character_count = get_character_count(text)
    character_count_list = get_character_count_list(character_count)
    character_count_list.sort(reverse=True, key=sort_character_count)
    for character_counts in character_count_list:
        print(f"The {character_counts["char"]} character was found {character_counts["num"]} times")
    print("--- End report ---")


def get_book_path():
    path_input = input("Enter file location: ")
    return path_input


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
    
def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    character_dict = {}
    lower_case_text = text.lower()
    for character in lower_case_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict


def get_character_count_list(character_dict):
    character_count_list = []
    for character, count in character_dict.items():
        if character.isalpha():
            single_entry_dict = {"char": character, "num": count}
            character_count_list.append(single_entry_dict)
    return character_count_list


def sort_character_count(character_count):
    return character_count["num"]


main()