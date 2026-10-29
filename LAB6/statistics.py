input_str = input("Введите целые числа через пробел: ")

nums = []
for part in input_str.split():
    nums.append(int(part))

if len(nums) == 0:
    print("Нет данных")
else:
    count = len(numbers)
    total_sum = sum(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    avg = total_sum / count
    
    print(f"Количество: {count}")
    print(f"Сумма: {total_sum}")
    print(f"Минимум: {min_val}")
    print(f"Максимум: {max_val}")
    print(f"Среднее: {avg:.2f}")