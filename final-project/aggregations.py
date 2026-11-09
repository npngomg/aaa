
from statistics import mean, median
from typing import Any, Optional, Union


def count_records(data: list[dict[str, Any]]) -> int:
    """Возвращает количество записей."""
    return len(data)


def calculate_mean(
    data: list[dict[str, Any]],
    attribute: str,
) -> Optional[float]:
    """Рассчитывает среднее значение атрибута."""
    values = [
        item[attribute]
        for item in data
        if isinstance(item.get(attribute), (int, float))
        and not isinstance(item[attribute], bool)
    ]

    return mean(values) if values else None


def calculate_median(
    data: list[dict[str, Any]],
    attribute: str,
) -> Optional[Union[int, float]]:
    """Рассчитывает медиану атрибута."""
    values = [
        item[attribute]
        for item in data
        if isinstance(item.get(attribute), (int, float))
        and not isinstance(item[attribute], bool)
    ]

    return median(values) if values else None


def calculate_max(
    data: list[dict[str, Any]],
    attribute: str,
) -> Optional[Union[int, float]]:
    """Возвращает максимальное значение атрибута."""
    values = [
        item[attribute]
        for item in data
        if isinstance(item.get(attribute), (int, float))
        and not isinstance(item[attribute], bool)
    ]

    return max(values) if values else None


def top_n(
    data: list[dict[str, Any]],
    attribute: str,
    n: int = 5,
) -> list[dict[str, Any]]:
    """Возвращает топ-N записей по убыванию атрибута."""
    valid_data = [
        item for item in data
        if isinstance(item.get(attribute), (int, float))
        and not isinstance(item[attribute], bool)
    ]

    return sorted(
        valid_data,
        key=lambda item: item[attribute],
        reverse=True,
    )[:n]
