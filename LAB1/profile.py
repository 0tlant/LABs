last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст: "))
favorite_subject = input("Введите любимый предмет: ")
hours_per_week = float(input("Введите количество часов подготовки в неделю: "))

full_name = f"{first_name} {last_name}"
age_in_4_years = age + 4
hours_in_4_weeks = hours_per_week * 4
daily_hours = hours_per_week / 7

print("\n--- КАРТОЧКА СТУДЕНТА ---")
print(f"Студент: {full_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Возраст через 4 года: {age_in_4_years}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Часов в неделю: {hours_per_week:.2f}")
print(f"Часов за 4 недели: {hours_in_4_weeks:.2f}")
print(f"Часов в день (в среднем): {daily_hours:.2f}")
