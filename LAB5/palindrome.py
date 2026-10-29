text = input("Введите текст: ")

x = text.replace(" ", "").lower()

if len(cleaned) == 0:
    print("Нет текста")
else:
    if x == x[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")