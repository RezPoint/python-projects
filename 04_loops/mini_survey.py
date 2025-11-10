print("Привет! Мы проведем мини-опрос.\n")

numbers = []

while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break  # Выходим из цикла, если введён 0
    numbers.append(num)  # Добавляем число в список

print("\nВы ввели числа:", numbers)

# Проверка каждого числа
for n in numbers:
    if n % 2 == 0:
        print(f"{n} — чётное")
    else:
        print(f"{n} — нечётное")
