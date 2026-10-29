n = int(input("Введите количество чисел (n >= 1): "))

first_num = int(input("Введите число: "))

total_sum = first_num
count = 0
max_num = first_num

if first_num > 0:
    positive_count += 1

for _ in range(n - 1):
    num = int(input("Введите число: "))
    
    total_sum += num
    if num > 0:
        count += 1
    if num > max_num:
        max_num = num

print(f"Сумма: {total_sum}")
print(f"Количество положительных: {count}")
print(f"Максимум: {max_num}")