"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def count_sold_avg(product_sold):
    sold_sum = 0
    for sold in product_sold:
        sold_sum += sold
    return sold_sum / len(product_sold)


def count_sold_avg(product_sold):
    sold_sum_avg = 0
    for sold in product_sold:
        sold_sum_avg += sold
    return sold_sum_avg / len(product_sold)


def count_sold_all(product_sold):
    sold_sum_by_phone = 0
    for sold in product_sold:
        sold_sum_by_phone += sold
    return sold_sum_by_phone


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    avg_sold_phones = 0
    for phones in sold_phones:
        sold = round(count_sold_avg(phones['items_sold']), 2)  # округленный результат
        print(f'Avg sum of sales by phone {phones["product"]}: {sold}')
        avg_sold_phones += sold

    avg_sold_phones_all = round(avg_sold_phones / len(sold_phones), 2)
    print(f'Avg sum of sales for all phones: {avg_sold_phones_all}')

    all_sold_phones = 0
    for phones in sold_phones:
        sold = count_sold_all(phones['items_sold'])
        print(f'Sum of all phones sales by phone {phones["product"]}: {sold}')
        all_sold_phones += sold

    print(f'Sum of all phones sales {all_sold_phones}')


if __name__ == "__main__":
    sold_phones = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    main()
