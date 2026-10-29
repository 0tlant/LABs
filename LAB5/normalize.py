text = input("Введите строку: ")

1length = len(text)

normalized = " ".join(text.split())
2length = len(normalized)

words = normalized.split()
count = len(words)

print(f"Исходная длина: {1length}")
print(f"Новая длина: {2length}")
print(f"Нормализованный текст: {normalized}")
print(f"Количество слов: {count}")