"""
task_manager.py — тренируемся работать со списками и словарями.
Каждая задача — это словарь с полями title (название), status (состояние) и priority (приоритет).
"""

# Шаг 1. Стартовый список задач — заранее подготовленные элементы.
tasks = [
    {"title": "Выучить списки", "status": "в процессе", "priority": "высокий"},
    {"title": "Сделать домашку по Python", "status": "готово", "priority": "средний"},
    {"title": "Повторить циклы", "status": "новая", "priority": "низкий"},
]

print("=== Текущие задачи ===")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. [{task['status']}] {task['title']} (приоритет: {task['priority']})")

# Шаг 2. Добавляем новую задачу от пользователя.
print("\nДобавим новую задачу.")
new_title = input("Название задачи: ").strip()
new_priority = input("Приоритет (низкий/средний/высокий): ").strip() or "средний"

if new_title:
    tasks.append({"title": new_title, "status": "новая", "priority": new_priority})
    print("Задача добавлена!")
else:
    print("Название не указано — пропускаем добавление.")

# Шаг 3. Фильтрация по статусу.
print("\nХочешь увидеть задачи с конкретным статусом?")
filter_status = input("Введи статус (новая/в процессе/готово): ").strip().lower()

if filter_status:
    filtered_tasks = [task for task in tasks if task["status"] == filter_status]
    if filtered_tasks:
        print(f"\nЗадачи со статусом '{filter_status}':")
        for task in filtered_tasks:
            print(f"- {task['title']} (приоритет: {task['priority']})")
    else:
        print(f"\nЗадач со статусом '{filter_status}' пока нет.")
else:
    print("\nСтатус не выбран, показываем все задачи.")

# Шаг 4. Мини-статистика по статусам.
status_counts = {}
for task in tasks:
    status = task["status"]
    status_counts[status] = status_counts.get(status, 0) + 1

print("\n=== Статистика по статусам ===")
for status, count in status_counts.items():
    print(f"{status}: {count}")

print("\nВсего задач:", len(tasks))

