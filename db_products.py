"""Загрузка товаров из БД с расширенным выводом."""
import sqlite3
from tkinter import messagebox
from config import DB_PATH
from order_manager import get_product_quantity

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

def get_product_sizes(product_id):
    """
    Возвращает список размеров для товара.
    :param product_id: id товара
    :return: список размеров
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT размер FROM Товар WHERE id = ?", (product_id,))
    rows = cur.fetchall()
    conn.close()
    return [row[0] for row in rows if row[0]]

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

from error_handler import validate_positive_int

def add_to_order(self):
    """Обработчик кнопки «Добавить в заказ»."""
    # 1. Проверяем товар
    if not self.product:
        messagebox.showerror("Ошибка", "Товар не выбран")
        return

    # 2. Валидация количества
    ok, result = validate_positive_int(self.qty_var.get(), "Количество")
    if not ok:
        messagebox.showwarning("Ошибка ввода", result) # type: ignore
        return

    qty = result  # result — это число

    # 3. Проверяем, что количество не больше доступного
    current_qty = get_product_quantity(self.product[0])
    if qty > current_qty: # type: ignore
        messagebox.showwarning("Ошибка",
                               f"Доступно только {current_qty} шт.")
        return

    # 4. Вызываем callback
    if self.on_add_to_order:
        try:
            self.on_add_to_order(self.product, qty, self.size_var.get())
            messagebox.showinfo("Успех", f"Товар добавлен в заказ ({qty} шт.)")
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Ошибка заказа", f"Не удалось добавить товар:\n{e}")


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