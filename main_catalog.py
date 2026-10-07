"""Главное окно приложения с каталогом."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # <--- ДОБАВЛЕНЫ ЭТИ ИМПОРТЫ
from config import APP_TITLE, FONT_FAMILY
from catalog import create_product_card
from db_products import get_all_products

class CatalogWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry("900x700")
        self.build_ui()
        self.load_products()

    def build_ui(self):
        # Заголовок
        header = tk.Frame(self.root, bg="#D2F6E7")
        header.pack(fill="x")
        from PIL import Image, ImageDraw

        # === ДОБАВЛЯЕМ ЛОГОТИП (Задание 2) ===
        try:
            logo = Image.open("resources/logo.png").resize((50, 50))
            logo_photo = ImageTk.PhotoImage(logo)
            logo_label = tk.Label(header, image=logo_photo, bg="#D2F6E7")
            from PIL import Image, ImageDraw
            
            # ВАЖНО: Сохраняем ссылку на изображение, чтобы оно не исчезло
            logo_label.image = logo_photo   # type: ignore
            logo_label.pack(side="left", padx=10)
        except Exception as e:
            print(f"Не удалось загрузить логотип: {e}")

        # Текст заголовка
        tk.Label(header, text="КАТАЛОГ ТОВАРОВ", font=(FONT_FAMILY, 16, "bold"), bg="#D2F6E7").pack(pady=15)

        # Область с прокруткой
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.catalog_frame = tk.Frame(self.canvas, bg="white")

        self.catalog_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.catalog_frame, anchor="nw")
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def load_products(self):
        products = get_all_products()   # без db.
        for p in products:
            create_product_card(self.catalog_frame, p)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    CatalogWindow().run()