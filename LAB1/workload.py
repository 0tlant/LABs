subject1 = input("Введите название первого предмета: ")
lessons1 = int(input("Количество занятий в неделю: "))
duration1 = int(input("Продолжительность одного занятия (в минутах): "))

subject2 = input("Введите название второго предмета: ")
lessons2 = int(input("Количество занятий в неделю: "))
duration2 = int(input("Продолжительность одного занятия (в минутах): "))

available_hours = float(input("Введите доступное время на неделю (в часах): "))

time1_min = lessons1 * duration1
time2_min = lessons2 * duration2

total_min = time1_min + time2_min
total_hours = total_min / 60

free_hours = available_hours - total_hours
total_4_weeks_hours = total_hours * 4

print("\n--- РЕЗУЛЬТАТЫ ---")
print(f"Время на {subject1}: {time1_min} мин.")
print(f"Время на {subject2}: {time2_min} мин.")
print(f"Общая нагрузка: {total_min} мин. ({total_hours:.2f} ч.)")
print(f"Остаток свободного времени: {free_hours:.2f} ч.")
print(f"Нагрузка за 4 недели: {total_4_weeks_hours:.2f} ч.")