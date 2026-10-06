"""Модели данных для проекта УП.02."""

class Product:
    """Класс Товар."""
    def __init__(self, product_id, genre, author, title, price, quantity, cover):
        """
        Инициализация товара.
        :param product_id: идентификатор
        :param genre: жанр
        :param author: автор
        :param title: название
        :param price: цена
        :param quantity: количество
        :param cover: обложка (имя файла)
        """
        self.id = product_id
        self.genre = genre
        self.author = author
        self.title = title
        self.price = price
        self.quantity = quantity
        self.cover = cover

    def total(self):
        """Общая стоимость (цена × количество)."""
        return self.price * self.quantity

    def price_with_discount(self, discount_percent):
        """Цена со скидкой."""
        return self.price * (1 - discount_percent / 100)

    def indicator(self):
        """Индикатор «много/мало» (порог 5)."""
        return "много" if self.quantity > 5 else "мало"

    def info(self):
        """Строка с информацией о товаре."""
        return (f"{self.title} ({self.genre}, {self.author}): "
                f"{self.price} руб. × {self.quantity} = {self.total()} руб. "
                f"{self.indicator()}")

    def is_available(self):
        """Возвращает True, если количество > 0."""
        return self.quantity > 0