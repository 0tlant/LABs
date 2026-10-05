price = int(input("Введите цену тетради (руб): "))

count_input = input("Введите количество: ")
while count_input == "":
    count_input = input("Количество не может быть пустым! Введите количество: ")
count = int(count_input)

paid_input = input("Введите переданную сумму (руб): ")
while paid_input == "":
    paid_input = input("Сумма не может быть пустой! Введите сумму: ")
paid = int(paid_input)

total_cost = price * count
change = paid - total_cost

print(f"Стоимость: {total_cost}")
print(f"Сдача: {change}")