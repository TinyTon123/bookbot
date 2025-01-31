from collections import Counter
from string import ascii_lowercase


def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    words_count = len(file_contents.split())
    letters_count = Counter(file_contents.lower())

    print(f'--- Begin report of {f.name} ---')
    print(f'{words_count} words found in the document\n')
    for letter in letters_count:
        if letter in ascii_lowercase:
            print(f"The '{letter}' character was found {letters_count[letter]} times")
    print('--- End report ---')

if __name__ == '__main__':
    main()
