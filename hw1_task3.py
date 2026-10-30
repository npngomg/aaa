from typing import Any

orders: list[dict[str, Any]] = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2100},
]

returned_amount = 0
returned_buyers = set()
delivered_count = 0
delivered_amount = 0

for order in orders:
    if order["status"] == "returned":
        returned_amount += order["amount"]
        returned_buyers.add(order["buyer"])

    if order["status"] == "delivered":
        delivered_count += 1
        delivered_amount += order["amount"]

# Общая сумма возвратов
print("Сумма возвратов:", returned_amount)

# Кто хотя бы раз возвращал заказ
print("Покупатели с возвратами:", returned_buyers)

# Количество доставленных заказов
print("Доставленных заказов:", delivered_count)

# Средний чек доставленных заказов
average_check = delivered_amount / delivered_count
print(f"Средний чек: {average_check:.2f}")
