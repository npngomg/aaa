from typing import Any

days: list[dict[str, Any]] = [
    {"day": "пн", "orders": 20, "revenue": 40000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48000, "returns": 3},
]

# Выручка за всю неделю
total_revenue = 0

for day in days:
    total_revenue += day["revenue"]

print("Выручка за неделю:", total_revenue)

# День с максимальной выручкой
best_day = max(days, key=lambda day: day["revenue"])
print("Самая большая выручка:", best_day["day"])

# Средняя выручка на один заказ
for day in days:
    average = day["revenue"] / day["orders"]
    print(f"{day['day']}: средняя выручка = {average:.2f}")

# Дни с долей возвратов больше 20%
for day in days:
    return_share = day["returns"] / day["orders"] * 100

    if return_share > 20:
        print(f"{day['day']}: возвратов {return_share:.2f}%")
