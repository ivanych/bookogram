import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def variants(p: dict):
    """
    Метод формирует кнопки выбора вариантов

    :param p:
    :return:
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            _random_variant(p) if p.get('random') == 'true' else _all_variants(p)
        ],
    )


def _all_variants(p: dict):
    return [
        InlineKeyboardButton(
            text=variant_id,
            callback_data=f"{p['book_id']}_{variant_id}"
        )
        for variant_id in list(p.get('answers'))
    ]


def _random_variant(p: dict):
    return [
        InlineKeyboardButton(
            text='  🎲  '.join(list(p.get('answers'))),
            callback_data=f"{p['book_id']}_{random.choice(list(p.get('answers')))}"
        )
    ]
