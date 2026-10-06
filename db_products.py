"""Загрузка товаров из БД с расширенным выводом."""
import sqlite3
from config import DB_PATH

def get_all_products():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар ORDER BY id")
    products = cur.fetchall()
    conn.close()
    return products

def get_products_by_category(category):
    """Товары по категории."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE жанр = ?", (category,))
    products = cur.fetchall()
    conn.close()
    return products

def get_products_low_stock():
    """Товары с количеством ≤ 3."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE количество <= 3")
    products = cur.fetchall()
    conn.close()
    return products

def get_categories():
    """Список всех категорий."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT жанр FROM Товар ORDER BY жанр")
    categories = [row[0] for row in cur.fetchall()]
    conn.close()
    return categories

def print_catalog(products):
    """Каталог с индикатором."""
    print(f"\n{'=' * 60}")
    print(f"КАТАЛОГ ({len(products)} товаров)")
    print("=" * 60)
    
    for p in products:
        product_id, genre, author, name, price, qty, cover = p
        # Индикатор: если количество <= 3, ставим "!", иначе "+"
        indicator = "!" if qty <= 3 else "+"
        print(f"[{indicator}] {name} ({author}) - {price} руб. | Остаток: {qty} шт.")

if __name__ == "__main__":
    print("=== ВСЕ ТОВАРЫ ===")
    all_products = get_all_products()
    print_catalog(all_products)
    
    print("\n=== ТОВАРЫ С НИЗКИМ ОСТАТКОМ (<= 3) ===")
    low_stock = get_products_low_stock()
    print_catalog(low_stock)
    
    print("\n=== СПИСОК КАТЕГОРИЙ ===")
    categories = get_categories()
    print(", ".join(categories))