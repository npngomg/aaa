
moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

# Товары в обоих городах
both_cities = moscow & kazan
print("Товары в обоих городах:", both_cities)

# Товары только в Москве
only_moscow = moscow - kazan
print("Только в Москве:", only_moscow)

# Товары только в Казани
only_kazan = kazan - moscow
print("Только в Казани:", only_kazan)

# Количество разных товаров
all_products = moscow | kazan
print("Всего разных товаров:", len(all_products))
