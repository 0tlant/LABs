total = int(input("Введите количество студентов (общий объем): "))
capacity = int(input("Введите мест в автобусе (вместимость): "))

full_units = total // capacity
remainder = total % capacity

total_units = (total + capacity - 1) // capacity

print(f"Полных: {full_units}, остаток {remainder}, всего {total_units}")