print("Привет! Мы проведем мини-опрос.\n")

numbers = []

while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break  # Выходим из цикла, если введён 0
    numbers.append(num)  # Добавляем число в список

print("\nВы ввели числа:", numbers)

if not numbers:
    print("Вы не ввели ни одного числа.")
else:
    total = sum(numbers)
    average = total / len(numbers)
    even_count = len([n for n in numbers if n % 2 == 0])
    odd_count = len(numbers) - even_count

    print("\nСтатистика:")
    print(f"Сумма: {total}")
    print(f"Среднее: {average}")
    print(f"Чётных чисел: {even_count}")
    print(f"Нечётных чисел: {odd_count}")
    print(f"Минимум: {min(numbers)}, максимум: {max(numbers)}")

    # Проверка каждого числа
    print("\nПроверим каждое число:")
    for n in numbers:
        if n % 2 == 0:
            print(f"{n} — чётное")
        else:
            print(f"{n} — нечётное")
