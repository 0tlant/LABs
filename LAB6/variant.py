input_str = input("Введите целые числа через пробел: ")

numbers = []
for part in input_str.split():
    numbers.append(int(part))

result = []
for num in numbers:

    x = (num % 2 == 0)
    
    if x:
        result.append(num)

count = len(result)
total_sum = sum(result)
sorted_copy = sorted(result)

print(f"Выборка: {result}")
print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
print(f"Сортированная копия: {sorted_copy}")