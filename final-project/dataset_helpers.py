
from typing import Any, Callable


def filter_data(
    data: list[dict[str, Any]],
    condition: Callable[[dict[str, Any]], bool],
) -> list[dict[str, Any]]:
    """Фильтрует список словарей по заданному условию."""
    return [item for item in data if condition(item)]


def group_by_attributes(
    data: list[dict[str, Any]],
    attributes: list[str],
) -> dict[tuple, list[dict[str, Any]]]:
    """Группирует записи по значениям указанных атрибутов."""
    groups = {}

    for item in data:
        key = tuple(item.get(attribute) for attribute in attributes)
        groups.setdefault(key, []).append(item)

    return groups



def aggregate_data(
    data: list[dict[str, Any]],
    aggregations: dict[
        str, Callable[[list[dict[str, Any]]], Any]
    ],
) -> dict[str, Any]:
    """Применяет агрегирующие функции к списку словарей."""
    return {
        name: function(data)
        for name, function in aggregations.items()
    }



def count_missing_values(
    data: list[dict[str, Any]],
) -> dict[str, int]:
    """Считает количество пропущенных значений по каждому полю."""
    attributes = set()

    for item in data:
        attributes.update(item.keys())

    return {
        attribute: sum(
            item.get(attribute) is None or item.get(attribute) == ''
            for item in data
        )
        for attribute in sorted(attributes)
    }


def find_id_gaps(
    data: list[dict[str, Any]],
    attribute: str = 'id',
) -> list[tuple[int, int]]:
    """Находит пары соседних ID, между которыми есть пропуски."""
    ids = sorted({
        item[attribute]
        for item in data
        if isinstance(item.get(attribute), int)
    })

    return [
        (left, right)
        for left, right in zip(ids, ids[1:])
        if right - left > 1
    ]

