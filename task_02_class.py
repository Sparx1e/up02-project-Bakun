class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return self.price * self.qty

    def info(self):
        return f"{self.name}: {self.price} × {self.qty} = {self.total()} руб."

products = [
    Product("Война и мир", 1500, 5),
    Product("Мастер и Маргарита", 1200, 8),
    Product("Происхождение видов", 1800, 2),
]

for p in products:
    print(p.info())