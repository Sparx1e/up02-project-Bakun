"""Форма просмотра товара."""
import tkinter as tk
from tkinter import ttk, messagebox

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
        """Строит интерфейс формы."""
        # Шапка — ГОТОВО
        header = tk.Frame(self.window, bg=COLOR_SECONDARY_BG, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text="КАРТОЧКА ТОВАРА",
                 font=font(FONT_SIZE_TITLE, bold=True),
                 bg=COLOR_SECONDARY_BG).pack(pady=15)
        
        # Основная область — ГОТОВО
        main = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        main.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Изображение — ГОТОВО
        img_frame = tk.Frame(main, bg=COLOR_MAIN_BG)
        img_frame.pack(side="left", padx=10)
        
        photo = get_product_image(self.product[7], size=(200, 200))
        if photo:
            img_label = tk.Label(img_frame, image=photo, bg=COLOR_MAIN_BG)
            img_label.image = photo # type: ignore
            img_label.pack()
        
        # Информация — ДОПИШИТЕ
        info_frame = tk.Frame(main, bg=COLOR_MAIN_BG)
        info_frame.pack(side="left", fill="both", expand=True, padx=20)
        
        # TODO: добавить поля через _add_field
        self._add_field(info_frame, "Производство", self.product[3])
        self._add_field(info_frame, "Наименование", self.product[1])
        self._add_field(info_frame, "Категория", self.product[2])
        self._add_field(info_frame, "Состав", self.product[4])
        self._add_field(info_frame, "Цена", f"{self.product[5]} руб.")
        self._add_field(info_frame, "Размеры", self.product[8])
        
        # Кнопки — ДОПИШИТЕ
        btn_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        btn_frame.pack(fill="x", pady=10)
        
        # TODO: кнопка "Добавить в заказ" -> self.add_to_order
        btn_add = tk.Button(
            btn_frame, text="Добавить в заказ", command=self.add_to_order,
            bg=COLOR_ACCENT, fg="white", font=font(FONT_SIZE_NORMAL), padx=15, pady=5
        )
        btn_add.pack(side="left", padx=20)
        
        # TODO: кнопка "Назад" -> self.window.destroy
        btn_back = tk.Button(
            btn_frame, text="Назад", command=self.window.destroy,
            bg=COLOR_ACCENT, fg="white", font=font(FONT_SIZE_NORMAL), padx=15, pady=5
        )
        btn_back.pack(side="right", padx=20)
    
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
    
    def add_to_order(self):
        """Обработчик кнопки «Добавить в заказ»."""
        if not self.on_add_to_order:
            messagebox.showinfo("Информация", "Функция в разработке")
            return
            
        if not self.product:
            messagebox.showerror("Ошибка", "Товар не выбран")
            return
            
        try:
            self.on_add_to_order(self.product)
            messagebox.showinfo("Успех", "Товар добавлен в заказ")
        except Exception as e:
            messagebox.showerror("Ошибка заказа", f"Не удалось добавить товар:\n{e}")
        pass
    