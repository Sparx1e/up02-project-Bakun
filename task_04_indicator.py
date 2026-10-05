catalog = [
    {"name": "Происхождение видов", "price": 1800, "qty": 2},
    {"name": "Мастер и Маргарита", "price": 1500, "qty": 8},
    {"name": "Война и мир", "price": 1200, "qty": 5},
    {"name": "Доктор Айболит", "price": 500, "qty": 15},
    {"name": "Евгений Онегин", "price": 800, "qty": 10},
]

print("Каталог с индикатором:")
sorted_catalog = sorted(catalog, key=lambda x: x["qty"] <= 5)  # сначала «много»

for i, item in enumerate(sorted_catalog, 1):
    mark = "много" if item["qty"] > 5 else "мало"
    print(f"{i}. {item['name']} – {item['qty']} шт. → {mark}") 
