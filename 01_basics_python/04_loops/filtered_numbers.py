valid_numbers = []
skipped = 0

for i in range(10):
    value = int(input(f"Введите число {i+1}: "))
    if value < 0:
        skipped += 1
        continue
    valid_numbers.append(value)

print("\nИтоги:")
if valid_numbers:
    print("Введённые числа:", valid_numbers)
    print("Сумма введённых чисел:", sum(valid_numbers))
    average = sum(valid_numbers) / len(valid_numbers)
    print("Среднее значение:", round(average, 2))
else:
    print("Вы не ввели ни одного неотрицательного числа.")

print("Количество пропущенных (отрицательных) чисел:", skipped)