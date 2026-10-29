try = 0

while True:
    num = int(input("Введите целое число: "))
    if num > 0:
        break  
    try += 1

print(f"Квадрат числа: {num ** 2}")
print(f"Количество отклонённых попыток: {try}")