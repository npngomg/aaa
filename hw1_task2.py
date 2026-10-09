
queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

# Всего поисковых запросов
total = len(queries)
print("Всего запросов:", total)

# Сколько раз встречается каждый запрос
counts = {}

for query in queries:
    if query not in counts:
        counts[query] = 0
    counts[query] += 1

print("Количество каждого запроса:", counts)

# Самый популярный запрос
most_popular = max(counts, key=lambda query: counts[query])
print("Самый популярный запрос:", most_popular)

# Доля самого популярного запроса
share = counts[most_popular] / total * 100
print(f"Доля самого популярного запроса: {share:.2f}%")

# Запросы, которые встречались один раз
for query in counts:
    if counts[query] == 1:
        print("Встретился один раз:", query)
