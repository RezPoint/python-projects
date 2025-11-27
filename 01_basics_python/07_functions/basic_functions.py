"""
basic_functions.py — первые шаги с функциями в Python.
Функция — это переиспользуемый блок кода, который можно вызвать по имени.
"""


def greet_user(name):
    """Простая функция: принимает имя и печатает приветствие."""
    print(f"Привет, {name}! Рад видеть твоё прогресс в Python.")


def calculate_average(numbers):
    """
    Функция с возвратом значения.
    Принимает список чисел и возвращает среднее.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def describe_student(name, age, grade=5.0):
    """
    Функция с аргументом по умолчанию.
    Если grade не передать — будет 5.0.
    """
    return f"{name}, {age} лет — оценка {grade}"


# === Тестируем функции ===
greet_user("RezPoin")

grades = [4.5, 5.0, 3.8, 4.2]
average_grade = calculate_average(grades)
print(f"Средний балл: {round(average_grade, 2)}")

student_info = describe_student("Аня", 19, 4.5)
print(student_info)

