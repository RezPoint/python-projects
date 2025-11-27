shopping = ["молоко", "хлеб", "яйца"]
print("Стартовый список покупок:", shopping)

shopping.append("сыр")
print("После добавления сыра:", shopping)

shopping.insert(1, "фрукты")
print("После вставки фруктов:", shopping)

extra_item = input("Что ещё добавить в список? ")
if extra_item.strip():
    shopping.append(extra_item)
    print("После добавления твоего товара:", shopping)

if "яйца" in shopping:
    shopping.remove("яйца")
    print("После удаления яиц:", shopping)
else:
    print("Яиц в списке не было, ничего не удаляем.")

print("\nИтоговый список покупок:", shopping)
print("Всего товаров:", len(shopping))
print("Первые два товара:", shopping[:2])
print("Последние два товара:", shopping[-2:])