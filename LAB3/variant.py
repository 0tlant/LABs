#(пример вариант 1 — Заряд аккумулятора)

charge = int(input("Введите уровень заряда (0-100): "))

if charge < 0 or charge > 100:
    print("Ошибка диапазона")
elif 0 <= charge <= 19:
    print("Низкий")
elif 20 <= charge <= 79:
    print("Средний")
else:
    print("Высокий")