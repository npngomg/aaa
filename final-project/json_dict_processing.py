
from typing import Any, Callable


def extract_nested_value(
    obj: dict[str, Any],
    keys: list[str],
) -> Any:
    """Извлекает значение по цепочке ключей."""
    value = obj

    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)

    return value


def process_dictionary_with_config(
    dictionary: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    """Обрабатывает словарь согласно конфигурации."""
    result = {}

    for attribute, rule in config.items():
        if isinstance(rule, tuple):
            keys, processor = rule
        else:
            keys, processor = rule, None

        value = extract_nested_value(dictionary, keys)

        if processor is not None and value is not None:
            value = processor(value)

        result[attribute] = value

    return result


def process_list_of_dicts_with_config(
    list_of_dicts: list[dict[str, Any]],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    """Обрабатывает список словарей."""
    return [
        process_dictionary_with_config(item, config)
        for item in list_of_dicts
    ]


def create_processor(
    config: dict[str, Any],
    list_processor: bool = False,
) -> Callable:
    """Создаёт функцию обработки с заданной конфигурацией."""
    def processor(data: Any) -> Any:
        if list_processor:
            return process_list_of_dicts_with_config(data, config)

        return process_dictionary_with_config(data, config)

    return processor
