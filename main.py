def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    sorted_report = get_report(letter_count)

    print(f" --- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document!")
    print()

    for item in sorted_report:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item["num"]} times")

    print("--- End report ---")

    

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


def sort_on(d):
    return d["num"]

def get_report(letter_count):
    sorted_letters = []
    for ch in letter_count:
        sorted_letters.append({"char": ch, "num": letter_count[ch]})
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters
    
main()
