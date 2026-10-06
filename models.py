"""Модели данных для проекта УП.02."""
from datetime import datetime
from discount import calculate_price_with_discount

class Order:
    def __init__(self, id, date, client, product_id, quantity):
        self.id = id
        self.date = date
        self.client = client
        self.product_id = product_id
        self.quantity = quantity

    def order_info(self):
        return f"Заказ №{self.id} от {self.date}: {self.client}"    
        return f"Заказ №{self.id} от {self.date}: {self.client}"

class Product:
    def is_available(self):
        """Товар доступен для заказа?"""
        return self.quantity > 0
    """Класс Товар."""
    def discounted_price(self):
        """Цена со скидкой 25% (упрощённо)."""      
        return self.price * 0.75
    def __init__(self, product_id, name, category, price, quantity):
        self.id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

    def price_with_discount_auto(self, date=None):
        """Цена со скидкой по алгоритму ДЭ."""
        if date is None:
            date = datetime.now()
        return calculate_price_with_discount(self.id, self.price, date)

    def indicator(self):
        return "много" if self.quantity > 5 else "мало"

    def info(self):
        return (
            f"{self.name} ({self.category}): "
            f"{self.price} руб. × {self.quantity} = {self.total()} руб."
        )
    