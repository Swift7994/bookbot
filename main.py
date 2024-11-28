def main():
    book_path = get_book_path()
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print(text)
    print(f"Word count: {word_count}")
    print(f"Character count: {character_count}")

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
    alphabetical_dict = {key: character_dict[key] for key in sorted(character_dict)}
    return alphabetical_dict

main()