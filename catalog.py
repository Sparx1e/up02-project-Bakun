"""Каталог товаров."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from config import DB_PATH, COLOR_HIGHLIGHT, FONT_FAMILY


def create_product_card(parent, product):
    """
    Создаёт карточку товара по макету.
    
    :param parent: родительский контейнер
    :param product: кортеж из БД
    """
    # Определяем фон: подсветка, если количество ≤3
    qty = product[5]   # ⚠️ Замените индекс на свой!
    bg_color = COLOR_HIGHLIGHT if qty <= 3 else "white"

    # Карточка — рамка со всех сторон
    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    # === Изображение (слева) ===
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    image_path = product[6] if product[6] else r"C:\Users\funny\OneDrive\Рисунки\Screenshots\image.png"
    if not os.path.exists(image_path):
        image_path = "resources/picture.png"

    try:
        img = Image.open(image_path).resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        img_label.image = photo   # type: ignore # сохраняем ссылку!
        img_label.pack()
    except Exception:
        tk.Label(img_frame, text="[ФОТО]", bg=bg_color,
                 width=10, height=5).pack()

    # === Текстовая часть (справа) ===
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # Производство | Наименование
    title = f"{product[1]} | {product[3]}"
    tk.Label(text_frame, text=title, font=(FONT_FAMILY, 14, "bold"),
             bg=bg_color, anchor="w").pack(fill="x")

    # Автор
    tk.Label(text_frame, text=f"Автор: {product[2]}",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # Количество
    indicator = "много" if qty > 5 else "мало"
    tk.Label(text_frame, text=f"Количество: {indicator} ({qty})",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # Жанр
    tk.Label(text_frame, text=f"Жанр: {product[1]}",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # Цена (справа)
    tk.Label(text_frame, text=f"{product[4]} руб.",
             font=(FONT_FAMILY, 14, "bold"),
             bg=bg_color, anchor="e").pack(fill="x")

    return card