from catalog import create_product_card
from error_handler import safe_call

def load_products(self, db):
    """Загружает товары с обработкой ошибок."""
    products = safe_call(db.get_all_products) or []
    for p in products:
        safe_call(create_product_card, self.catalog_frame, p)

def refresh_catalog(self):
    """Обновляет каталог."""
    # Удаляем все существующие карточки
    for widget in self.catalog_frame.winfo_children():
        widget.destroy()

    # Загружаем товары заново
    self.load_products()