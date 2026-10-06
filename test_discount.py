"""Тестирование алгоритма скидки."""
from datetime import datetime
from discount import calculate_price_with_discount


def run_tests():
    """Прогон тестов."""
    date = datetime(2026, 10, 15)

    test_cases = [
        # (id, цена, ожидание, пояснение)
        (1, 8500, 8500, "Классика — есть заказы в сентябре"),
        (2, 15000, 11250, "Детское — нет заказов → 25% скидка"),
        (3, 12000, 12000, "Научное — есть заказы"),
        (4, 4500, 3375, "Детектив — нет заказов → скидка"),
        (5, 6000, 4500, "Поэзия — нет заказов → скидка"),
    ]

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ")
    print("=" * 60)

    passed = 0
    for product_id, price, expected, comment in test_cases:
        result = calculate_price_with_discount(product_id, price, date)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} Товар {product_id}: {price} → {result} "
              f"(ожидалось {expected}) — {comment}")

    print("=" * 60)
    print(f"Пройдено: {passed} / {len(test_cases)}")


if __name__ == "__main__":
    run_tests()
