"""Работа с заказами."""
import sqlite3
from datetime import datetime
from config import DB_PATH


def get_connection():
    """Соединение с БД."""
    return sqlite3.connect(DB_PATH)

def add_order_to_db(client, product_id, quantity):
    """Добавляет новый заказ в БД."""
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        date_str = datetime.now().strftime("%Y-%m-%d")

        cur.execute(
            "INSERT INTO Заказ (дата, клиент, товар_id, количество) VALUES (?, ?, ?, ?)",
            (date_str, client, product_id, quantity)
        )
        conn.commit()
        order_id = cur.lastrowid
        return order_id
    except Exception as e:
        print(f"Ошибка add_order_to_db: {e}")
        return None
    finally:
        if conn:
            conn.close()
    pass

def update_product_quantity(product_id, new_quantity):
    """Обновляет количество товара в БД."""
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE Товар SET количество = ? WHERE id = ?",
            (new_quantity, product_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Ошибка update_product_quantity: {e}")
        return False
    finally:
        if conn:
            conn.close()
    pass


def get_last_order_id():
    """Возвращает id последнего заказа."""
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT MAX(id) FROM Заказ")
        row = cur.fetchone()
        return row[0] if row and row[0] is not None else None
    except Exception as e:
        print(f"Ошибка get_last_order_id: {e}")
        return None
    finally:
        if conn:
            conn.close()
    pass


def get_product_quantity(product_id):
    """
    Возвращает количество товара по id.
    
    :param product_id: id товара
    :return: количество или 0
    """
    # ГОТОВО
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT количество FROM Товар WHERE id = ?", (product_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else 0