text = input("Введите строку: ")

count = text.count(":")

2text = text.replace(":", "-")

print(f"Количество замен: {count}")
print(f"Новая строка: {2text}")