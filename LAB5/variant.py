text = input("Введите строку: ")

words = text.split()
count = 0

for word in words:
    x = word.strip(".,!?;:").lower()
    
    if not x:
        continue
        
    a = x.startswith("а")
    
    if a:
        print(x)
        count += 1

if count == 0:
    print("Нет совпадений")

print(f"Количество: {count}")