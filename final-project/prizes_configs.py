
from typing import Any, Callable

from json_dict_processing import create_processor


CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], int),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus'],
    'motivation': ['motivation', 'en'],
}


def prize_processor() -> Callable[[Any], Any]:
    """Создает процессор для списка Нобелевских премий."""
    return create_processor(CONFIG_PRIZE, list_processor=True)
