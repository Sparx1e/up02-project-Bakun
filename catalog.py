"""Каталог товаров (Вариант 21 - Книги)."""

import tkinter as tk
from styles import (
    COLOR_MAIN_BG, COLOR_HIGHLIGHT,
    FONT_FAMILY, FONT_SIZE_NORMAL, FONT_SIZE_HEADER, font
)
from resources import get_product_image

def create_product_card(parent, product):
    """Создаёт карточку товара по макету."""
    # Индекс 5 — это количество (product[5])
    qty = product[5] 
    bg_color = _get_card_color(qty)

    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    _add_image(card, product, bg_color)
    _add_text_info(card, product, bg_color, qty)

    return card

def _get_card_color(qty):
    """Возвращает цвет фона карточки."""
    return COLOR_HIGHLIGHT if qty <= 3 else COLOR_MAIN_BG

def _add_image(card, product, bg_color):
    """Добавляет изображение товара (или заглушку)."""
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    # Индекс 6 — это обложка (product[6])
    photo = get_product_image(product[6], size=(100, 100)) 
    
    if photo:
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        img_label.image = photo  # type: ignore
        img_label.pack()
    else:
        tk.Label(img_frame, text="[НЕТ ФОТО]", bg=bg_color,
                 width=10, height=5).pack()

def _add_text_info(card, product, bg_color, qty):
    """Добавляет текстовую информацию о товаре (с обработкой крайних случаев из 5.4)."""
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # === ЗАДАНИЕ 5.4. Обработка крайних случаев (Вариант 21) ===
    # Индексы: 1 - жанр, 2 - автор, 3 - название, 4 - цена
    category = product[1] if product[1] else "[Без жанра]"
    author = product[2] if product[2] else "[Без автора]"
    name = product[3] if product[3] else "[Без названия]"
    price = product[4] if product[4] is not None else 0
    
    # В вашей БД нет поля "Состав", поэтому ставим заглушку
    composition = "[Не указан]"

    # Вывод текста на экран
    _add_label(text_frame, f"{author} | {name}",
               bg_color, bold=True, size=FONT_SIZE_HEADER)
    _add_label(text_frame, f"Категория (Жанр): {category}", bg_color)
    _add_label(text_frame, f"Количество: {_indicator(qty)} ({qty})", bg_color)
    _add_label(text_frame, f"Состав: {composition}", bg_color)
    _add_label(text_frame, f"{price} руб.",
               bg_color, bold=True, size=FONT_SIZE_HEADER, align="e")

def _add_label(parent, text, bg_color, bold=False,
               size=FONT_SIZE_NORMAL, align="w"):
    """Добавляет метку с текстом."""
    tk.Label(parent, text=text, font=font(size, bold=bold),
             bg=bg_color, anchor=align).pack(fill="x") # type: ignore

def _indicator(qty):
    """Индикатор «много/мало» (порог 5)."""
    return "много" if qty > 5 else "мало"