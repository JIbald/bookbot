def text_from_file(path):
    with open(path) as file:
        return file.read()

def main():
    print(text_from_file("./books/frankenstein.txt"))

main()
