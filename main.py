def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print(f"{word_count} words found in the document!")
    print(f"Here is how many times each character was used in this book: {letter_count}")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
        words = text.split()
        return len(words)
            
def count_letters(text):
    letters = {}
    lower_text = text.lower()
    for char in lower_text:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

main()
