"""Проверка вывода полей."""
from db_products import get_all_products

def test_prices():
    """Проверяет, что у всех товаров есть цена."""
    products = get_all_products() 
    for p in products:
        if p[4] is None:  # ⚠️ индекс цены для вашего варианта
            print(f"❌ Товар id={p[0]}: нет цены")
            return
    print("✅ У всех товаров есть цена")

def test_quantities():
    """Проверяет, что количество >= 0."""
    products = get_all_products() 
    for p in products:
        if p[5] is not None and p[5] < 0: # ⚠️ индекс количества
            print(f"❌ Товар id={p[0]}: отрицательное количество")
            return
    print("✅ У всех товаров корректное количество")

def test_has_image():
    """Проверяет, что хотя бы у одного товара есть изображение."""
    products = get_all_products() 
    has_img = any(p[6] for p in products) # ⚠️ индекс обложки
    if has_img:
        print("✅ Найдено изображение хотя бы у одного товара")
    else:
        print("❌ Ни у одного товара нет изображения")

def test_fields():
    """Проверяет, что все поля на месте."""
    products = get_all_products() 
    print(f"Всего товаров: {len(products)}")

    required_count = 6   # минимум полей для макета
    errors = 0

    for p in products:
        if len(p) < required_count:
            print(f"❌ Товар id={p[0]}: мало полей ({len(p)})")
            errors += 1

    if errors == 0:
        print("✅ Все товары содержат нужные поля")
    else:
        print(f"❌ Найдено ошибок: {errors}")


if __name__ == "__main__":
    test_fields()
