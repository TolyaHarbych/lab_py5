import re

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            print(f"Перше речення з файлу: {first_line}")
            return first_line
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}. Неможливо відкрити файл.")
        return None

def extract_words(sentence):
    if sentence is not None:
        words = re.findall(r'\b\w+\b', sentence)
        return words
    return []

def sort_and_count_words(words):
    if words:
        ukrainian_words = [word for word in words if any(char.isalpha() and ord(char) > 127 for char in word)]
        english_words = [word for word in words if all(not char.isalpha() or ord(char) <= 127 for char in word)]

        ukrainian_words = sorted(ukrainian_words, key=lambda s: s.lower())
        english_words = sorted(english_words, key=lambda s: s.lower())

        print("\nСлова українською мовою:")
        for word in ukrainian_words:
            print(word)
        print(f"Кількість українських слів: {len(ukrainian_words)}")

        print("\nEnglish words:")
        for word in english_words:
            print(word)
        print(f"Number of English words: {len(english_words)}")

def main():
    file_path = 'text.txt' 
    sentence = read_first_sentence(file_path)

    if sentence is not None:
        words = extract_words(sentence)
        sort_and_count_words(words)

if __name__ == "__main__":
    main()
