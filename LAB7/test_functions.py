from functions import sum_x, average, norm_text, select_nums

assert sum_x(0) == 0
assert sum_x(507) == 12
assert sum_x(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert norm_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert norm_text("   ") == ""

test_list = [-5, 0, 2, 5]
a = 2

assert select_nums(test_list, a) == [5]

assert select_nums([], a) == []

orig_list = [-5, 0, 2, 5]
_ = select_nums(original_list, a)
assert original_list == [-5, 0, 2, 5], "Исходный список был изменен!"

print("Базовые проверки пройдены")