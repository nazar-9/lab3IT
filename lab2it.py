# Кількість чисел для обчислення
n = int(input("Введіть кількість чисел: "))

# Змінна для зберігання суми
total = 0

for i in range(n):
    number = float(input(f"Введіть число {i + 1}: "))
    total += number

print(f"Сума введених чисел: {total}")

input()
