input_str = input("Введите целые числа через пробел: ")

nums = []
for part in input_str.split():
    nums.append(int(part))

if len(nums) == 0:
    print("Нет данных")
else:
    max_val = max(nums)
    posit = []
    
    for index, value in enumerate(nums):
        if value == max_val:
            posit.append(index)
            
    print(posit)