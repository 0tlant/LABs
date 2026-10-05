print("=== Фрагмент А ===")
first = "2"
second = "3"

print("Тип 'first' до:", type(first))
print("Тип 'second' до:", type(second))

first_num = int(first)
second_num = int(second)

print("Тип 'first' после:", type(first_num))
print("Тип 'second' после:", type(second_num))

result_a = first_num + second_num
print("Сумма чисел:", result_a)

print("=== Фрагмент Б ===")
age_str = input("Возраст: ")

print("Тип возраста до:", type(age_str))

age = int(age_str)

print("Тип возраста после:", type(age))

next_age = age + 1
print("Возраст через год:", next_age)

print("=== Фрагмент В ===")
first = 4
second = 7
third = 10

average = (first + second + third) / 3
print("Среднее арифметическое трех чисел:", average)
