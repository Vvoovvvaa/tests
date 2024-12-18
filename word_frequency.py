import string
from collections import Counter

stop_words = {
    'он', 'она', 'это', 'в', 'на', 'по', 'для', 'о', 'и', 'или', 'что', 'с', 'мы', 'вы', 'они', 'а', 'но'
}
def clean_text(text):
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def count_words(file_path, top_n=5):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        text = clean_text(text)
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words and word.isalpha()]
        word_counts = Counter(filtered_words)
        most_common = word_counts.most_common(top_n)

        print(f"Топ-{top_n} слов:")
        for word, count in most_common:
            print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден. Проверьте путь.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = input("Введите путь к текстовому файлу: ").strip()
count_words(file_path, top_n=5)
