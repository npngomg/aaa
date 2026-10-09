from typing import Any

reviews: list[dict[str, Any]] = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "чехол", "stars": 3},
    {"id": 1, "product": "ЧЕХОЛ", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

# Приводим названия к одному формату
for review in reviews:
    review["product"] = review["product"].strip().lower()

# Собираем оценки каждого товара
product_stars: dict[str, list[int]] = {}

for review in reviews:
    product = review["product"]

    if product not in product_stars:
        product_stars[product] = []

    product_stars[product].append(review["stars"])

# Средняя оценка каждого товара
average_ratings = {}

for product in product_stars:
    stars = product_stars[product]
    average = sum(stars) / len(stars)

    average_ratings[product] = average
    print(f"{product}: средняя оценка {average:.2f}")

# Худший товар среди тех, у кого минимум два отзыва
worst_product = ""
worst_rating = 6.0

for product in average_ratings:
    if len(product_stars[product]) >= 2:
        if average_ratings[product] < worst_rating:
            worst_rating = average_ratings[product]
            worst_product = product

print("Худший товар:", worst_product)

# Количество отзывов на 1 или 2 звезды
low_reviews = 0

for review in reviews:
    if review["stars"] <= 2:
        low_reviews += 1

print("Отзывов на 1-2 звезды:", low_reviews)

# Доля таких отзывов
share = low_reviews / len(reviews) * 100
print(f"Доля отзывов на 1-2 звезды: {share:.2f}%")
