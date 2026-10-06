"""Проверка класса Product."""
from models import Product

p = Product(
    product_id=1,
    genre="классика",
    author="Чехов",
    title="Вишневый сад",
    price=900,
    quantity=6,
    cover="chekhov.png"
)

print(p.info())
print(f"Со скидкой 25%: {p.price_with_discount(25):.2f} руб.")
print(f"В наличии: {p.is_available()}")