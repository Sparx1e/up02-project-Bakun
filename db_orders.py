"""Загрузка заказов из БД в объекты класса Order."""
import sqlite3
from config import DB_PATH
from models import Product, Order


def get_all_products_dict():
    """Возвращает словарь товаров по id."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар")
    rows = cur.fetchall()
    conn.close()

    products = {}
    for row in rows:
        product = Product(
            product_id=row[0],   # id
            genre=row[1],        # жанр
            author=row[2],       # автор
            title=row[3],        # название
            price=row[4],        # цена
            quantity=row[5],     # количество
            cover=row[6]         # обложка
        )
        products[product.id] = product
    return products


def get_all_orders():
    """Возвращает список объектов Order из БД."""
    products_dict = get_all_products_dict()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Заказ ORDER BY id")
    rows = cur.fetchall()
    conn.close()

    orders = []
    for row in rows:
        order_id = row[0]
        date = row[1]
        client = row[2]
        product_id = row[3]
        quantity = row[4]

        product = products_dict.get(product_id)
        if product:
            order = Order(order_id, date, client, product, quantity)
            orders.append(order)
    return orders


def print_orders(orders):
    """Выводит информацию о заказах."""
    print(f"\nВсего заказов: {len(orders)}\n")
    for o in orders:
        print(o.info())
        print(f"Сумма заказа: {o.total()} руб.")
        print("-" * 60)


if __name__ == "__main__":
    orders = get_all_orders()
    print_orders(orders)