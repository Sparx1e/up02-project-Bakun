price = float(input("Введите цену: "))
discount = float(input("Введите скидку (%): "))
final = price * (1 - discount / 100)
print(f"Цена со скидкой: {final:.2f} руб.")