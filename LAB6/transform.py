input_str = input("Введите целые числа через пробел: ")

orig = []
for part in input_str.split():
    orig.append(int(part))

trans = []
for num in orig:
    if num < 0:
        trans.append(abs(num))
    else:
        trans.append(num)

print(f"Исходный список: {orig}")
print(f"Новый список: {trans}")