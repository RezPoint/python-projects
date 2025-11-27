# students_data.py
# Пример работы со списками словарей
def print_students(title, students_list):
    print(f"\n{title}")
    if not students_list:
        print("Список студентов пуст.")
        return
    for student in students_list:
        print(f"{student['name']} ({student['age']} лет) — оценка: {student['grade']}")

# Список студентов (каждый студент — это словарь)
students = [
    {"name": "Аня", "age": 19, "grade": 4.5},
    {"name": "RezPoin", "age": 21, "grade": 5.0},
    {"name": "Марк", "age": 20, "grade": 3.8}
]

# 1️⃣ Выведем всех студентов
print_students("Все студенты:", students)

# 2️⃣ Найдем средний балл
total_grade = 0
for student in students:
    total_grade += student["grade"]

average_grade = total_grade / len(students)
print("\nСредний балл:", round(average_grade, 2))

# 3️⃣ Добавим нового студента
new_student = {"name": "Вика", "age": 18, "grade": 4.2}
students.append(new_student)
print_students("После добавления нового студента:", students)

# 4️⃣ Ищем конкретного студента
name_to_find = input("\nКого ищем по имени? ").strip()
found_student = None
for student in students:
    if student["name"].lower() == name_to_find.lower():
        found_student = student
        break

if found_student:
    print(f"Нашли: {found_student['name']} — оценка {found_student['grade']}, возраст {found_student['age']}")
else:
    print("Такого студента нет.")

# 5️⃣ Сортируем по оценке и показываем ТОП-3
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
top_students = sorted_students[:3]
print_students("ТОП-3 по оценке:", top_students)

# 6️⃣ Фильтруем по минимальному баллу
min_grade = float(input("\nМинимальная оценка для фильтра: "))
filtered_students = [s for s in students if s["grade"] >= min_grade]
print_students(f"Студенты с оценкой >= {min_grade}:", filtered_students)

# 7️⃣ Статистика
best_student = max(students, key=lambda s: s["grade"])
worst_student = min(students, key=lambda s: s["grade"])
high_achievers = sum(1 for s in students if s["grade"] >= 4)

print("\n=== Статистика ===")
print(f"Лучший студент: {best_student['name']} (оценка {best_student['grade']})")
print(f"Минимальный балл у: {worst_student['name']} (оценка {worst_student['grade']})")
print(f"Количество студентов с оценкой >= 4: {high_achievers}")
