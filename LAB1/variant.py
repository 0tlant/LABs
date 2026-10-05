order_name = input("Введите название заказа (например, Канцелярия): ")
customer_name = input("Введите имя заказчика: ")

item1_name = input("Название первой позиции (например, Тетради): ")
item1_count = int(input("Количество: "))
item1_price = float(input("Цена за единицу (руб): "))

item2_name = input("Название второй позиции (например, Ручки): ")
item2_count = int(input("Количество: "))
item2_price = float(input("Цена за единицу (руб): "))

delivery_cost = float(input("Стоимость доставки (руб): "))
paid_amount = float(input("Внесенная сумма (руб): "))

item1_total = item1_count * item1_price
item2_total = item2_count * item2_price

goods_total = item1_total + item2_total
grand_total = goods_total + delivery_cost

total_items = item1_count + item2_count
change = paid_amount - grand_total

print("\n" + "=" * 50)
print(f"ЗАКАЗ: {order_name}")
print(f"Заказчик: {customer_name}")
print("-" * 50)
print(f"{item1_name} | {item1_count} шт. | {item1_price:.2f} руб. | {item1_total:.2f} руб.")
print(f"{item2_name} | {item2_count} шт. | {item2_price:.2f} руб. | {item2_total:.2f} руб.")
print("-" * 50)
print(f"Общее количество товаров: {total_items} шт.")
print(f"Стоимость товаров без доставки: {goods_total:.2f} руб.")
print(f"Стоимость доставки: {delivery_cost:.2f} руб.")
print(f"Итого к оплате: {grand_total:.2f} руб.")
print(f"Внесено: {paid_amount:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
print("=" * 50)