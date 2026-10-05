first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print("\n--- До обмена ---")
print("Первая аудитория:", first_room)
print("Вторая аудитория:", second_room)

temp = first_room
first_room = second_room
second_room = temp

print("\n--- После обмена ---")
print("Первая аудитория:", first_room)
print("Вторая аудитория:", second_room)
