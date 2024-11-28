def main():
    book_path = get_book_path()
    text = get_book_text(book_path)
    print(text)

def get_book_path():
    path_input = input("Enter file location: ")
    return path_input


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()