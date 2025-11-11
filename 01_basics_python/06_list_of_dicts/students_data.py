# students_data.py
# Пример работы со списками словарей

# Список студентов (каждый студент — это словарь)
students = [
    {"name": "Аня", "age": 19, "grade": 4.5},
    {"name": "RezPoin", "age": 21, "grade": 5.0},
    {"name": "Марк", "age": 20, "grade": 3.8}
]

# 1️⃣ Выведем всех студентов
print("Список студентов:")
for student in students:
    print(f"{student['name']} ({student['age']} лет) — оценка: {student['grade']}")

# 2️⃣ Найдем средний балл
total_grade = 0
for student in students:
    total_grade += student["grade"]

average_grade = total_grade / len(students)
print("\nСредний балл:", round(average_grade, 2))

# 3️⃣ Добавим нового студента
new_student = {"name": "Вика", "age": 18, "grade": 4.2}
students.append(new_student)

# 4️⃣ Выведем обновленный список
print("\nПосле добавления нового студента:")
for student in students:
    print(f"{student['name']} — {student['grade']}")

# 5️⃣ Отфильтруем только отличников
excellent_students = [s for s in students if s["grade"] >= 4.5]
print("\nОтличники:")
for s in excellent_students:
    print(f"{s['name']} ({s['grade']})")
