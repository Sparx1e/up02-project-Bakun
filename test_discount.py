"""Тестирование алгоритма скидки для книжного магазина."""
from datetime import datetime
from discount import calculate_price_with_discount


def run_tests():
    test_cases = [
        # (product_id, price, date, expected, comment)
        # Базовые тесты на 15.10.2026 (предыдущий месяц — сентябрь 2026)
        (1, 900,  datetime(2026, 10, 15), 900,  "Классика — есть заказ в сентябре"),
        (2, 1100, datetime(2026, 10, 15), 1100, "Фантастика — есть заказ в сентябре"),
        (3, 1000, datetime(2026, 10, 15), 1000, "Детектив — есть заказ в сентябре"),
        (4, 700,  datetime(2026, 10, 15), 525,  "Поэзия — нет заказов → скидка 25%"),
        (5, 1800, datetime(2026, 10, 15), 1350, "Фэнтези — нет заказов → скидка 25%"),

        # Дополнительные тесты на другие даты
        (1, 900,  datetime(2026, 11, 15), 675,  "Ноябрь: за октябрь заказов нет → скидка"),
        (2, 1100, datetime(2026, 11, 15), 825,  "Ноябрь: за октябрь заказов нет → скидка"),
        (3, 1000, datetime(2026, 12, 15), 750,  "Декабрь: за ноябрь заказов нет → скидка"),
        (4, 700,  datetime(2026, 10, 1),  525,  "01.10.2026: предыдущий месяц сентябрь → скидка"),
        (5, 1800, datetime(2026, 8, 15),  1350, "Август: за июль заказов нет → скидка"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ (книжный магазин)")
    print("=" * 70)

    passed = 0
    for product_id, price, date, expected, comment in test_cases:
        result = calculate_price_with_discount(product_id, price, date)
        ok = abs(result - expected) < 0.01
        status = "✅" if ok else "❌"
        if ok:
            passed += 1
        print(
            f"{status} Товар {product_id}, дата {date:%d.%m.%Y}: "
            f"{price} → {result} (ожидалось {expected}) — {comment}"
        )

    print("=" * 70)
    print(f"Пройдено: {passed} / {len(test_cases)}")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()