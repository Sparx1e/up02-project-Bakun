"""Форма просмотра товара."""
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import messagebox
from db_products import get_product_sizes
from order_manager import (
    add_order_to_db,
)

from styles import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG, COLOR_ACCENT,
    FONT_SIZE_NORMAL, FONT_SIZE_HEADER, FONT_SIZE_TITLE, font
)
from resources import load_image, get_product_image


class ViewForm:
    """
    Форма просмотра выбранного товара.
    
    Открывается при клике на карточку в каталоге.
    """
    
    def __init__(self, parent, product, on_add_to_order=None):
        """
        Инициализация формы.
        
        :param parent: родительское окно
        :param product: кортеж с данными товара из БД
        :param on_add_to_order: callback для добавления в заказ
        """
        self.product = product
        self.on_add_to_order = on_add_to_order
        
        self.window = tk.Toplevel(parent)
        self.window.title(f"Просмотр — {product[1]}")
        self.window.geometry("700x600")
        self.window.configure(bg=COLOR_MAIN_BG)
        
        self.build_ui()
    
    def build_ui(self):
        # === Поле ввода количества ===
        qty_frame = tk.Frame(main, bg=COLOR_MAIN_BG) # type: ignore
        qty_frame.pack(fill="x", pady=10)

        tk.Label(qty_frame, text="Количество:", font=font(FONT_SIZE_NORMAL), 
         bg=COLOR_MAIN_BG).pack(side="left", padx=5)

        self.qty_var = tk.StringVar(value="1")
        qty_entry = tk.Entry(qty_frame, textvariable=self.qty_var, width=5, 
        font=font(FONT_SIZE_NORMAL))
        qty_entry.pack(side="left", padx=5)

        # === Выбор размера (если есть) ===
        size_frame = tk.Frame(main, bg=COLOR_MAIN_BG) # type: ignore
        size_frame.pack(fill="x", pady=10)

        tk.Label(size_frame, text="Размер:", font=font(FONT_SIZE_NORMAL), 
        bg=COLOR_MAIN_BG).pack(side="left", padx=5)

        # Получаем размеры из БД (если есть)
        sizes = get_product_sizes(self.product[0]) # Функция из db_products.py
        if not sizes:
            sizes = ["-"]

        self.size_var = tk.StringVar(value=sizes[0])
        size_combo = ttk.Combobox(size_frame, textvariable=self.size_var, 
                                values=sizes, state="readonly", width=5, 
                                font=font(FONT_SIZE_NORMAL))
        size_combo.pack(side="left", padx=5)
    
    def _add_field(self, parent, label, value):
        """
        Добавляет поле в форму.
        :param parent: родительский фрейм
        :param label: название поля (например, "Цена")
        :param value: значение (например, "8500 руб.")
        """
        row = tk.Frame(parent, bg=COLOR_MAIN_BG)
        row.pack(fill="x", pady=5)
        
        label_txt = tk.Label(
            row, text=f"{label}:", font=font(FONT_SIZE_NORMAL, bold=True),
            bg=COLOR_MAIN_BG, width=15, anchor="w"
        )
        label_txt.pack(side="left")
        
        value_txt = tk.Label(
            row, text=str(value), font=font(FONT_SIZE_NORMAL),
            bg=COLOR_MAIN_BG, anchor="w"
        )
        value_txt.pack(side="left")
    
    def add_to_order(self, qty):
        """Обработчик кнопки «Добавить в заказ»."""
        # ... валидация ...

        try:
            # Вызываем callback
            if self.on_add_to_order:
                self.on_add_to_order()

            messagebox.showinfo("Успех", f"Товар добавлен в заказ ({qty} шт.)")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось добавить товар:\n{e}")      