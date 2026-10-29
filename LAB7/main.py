from functions import sum_a, average, norm_text, select_nums

def main():
    num = int(input("Введите целое число для суммы цифр: "))
    print(f"Сумма цифр модуля: {sum_a(num)}")
    
    input_str = input("Введите числа через пробел для вычисления среднего: ")
    nums = [int(x) for x in input_str.split()]
    
    avg_result = average(nums)
    if avg_result is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {avg_result}")
        
    text = input("Введите произвольный текст для нормализации: ")
    print(f"Нормализованный текст: '{norm_text(text)}'")
    
    x = int(input("Введите порог (x) для фильтрации: "))
    b = select_nums(nums, x)
    print(f"Отфильтрованный список: {b}")

if __name__ == "__main__":
    main()