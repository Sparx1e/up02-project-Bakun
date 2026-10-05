catalog = [
    {"name": " Происхождение видов ", "price": 1800, "qty": 2},
    {"name": " Мастер и Маргарита ", "price": 1200, "qty": 8},
    {"name": " Война и мир ", "price": 1500, "qty": 5},
    {"name": " Доктор Айболит ", "price": 500, "qty": 15},
    {"name": " Евгений Онегин", "price": 800, "qty": 10},
]

print("Каталог товаров:")
total_sum = 0

for i, item in enumerate(catalog, 1):
    cost = item["price"] * item["qty"]
    total_sum += cost
    print(f"{i}. {item['name']} - {item['price']} x {item['qty']} = {cost} руб.")

print(f"Итого: {total_sum} руб.") 
