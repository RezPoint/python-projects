print("Привет! Мы сделаем простую статистику по введенным числам.")

numbers = []

while True:
    num  = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    numbers.append(num)
    
if len(numbers) == 0:
    print("Вы не ввели не одного числа.")
else:
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    
    
    print("\nВведенные числа:", numbers)
    print("Количество чисел:", count)
    print("Сумма:", total)
    print("Среднее:", average)
    print("Максимум:", maximum)
    print("Минимум:", minimum)
    