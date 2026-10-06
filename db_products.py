"""Загрузка товаров из БД."""
import sqlite3
from config import DB_PATH


def get_all_products():
    """Возвращает список всех товаров."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар ORDER BY id")
    products = cur.fetchall()
    conn.close()
    return products


def print_products(products):
    """Выводит товары в консоль."""
    print(f"\nВсего товаров: {len(products)}\n")
    for p in products:
        print(f"ID: {p[0]}")
        print(f"  Жанр: {p[1]}")
        print(f"  Автор: {p[2]} ")
        print(f"  Название: {p[3]} ")
        print(f"  Цена: {p[4]} руб.")
        print(f"  Количество: {p[5]} шт.")
        print("-" * 40)

if __name__ == "__main__":
    products = get_all_products()
    print_products(products)
    