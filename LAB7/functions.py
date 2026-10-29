def sum1(num):
    num = abs(num)  
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def average(nums):
    if len(nums) == 0:
        return None
    return sum(nums) / len(nums)


def text(text):
    return " ".join(text.split()).lower()


def select_nums(nums, x):
    result = []
    for num in nums:

        a = (num > x)
        
        if a:
            result.append(num)
            
    return result