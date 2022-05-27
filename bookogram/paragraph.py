import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def answers_ikm(p: dict):
    """
    Метод формирует кнопки выбора вариантов

    :param p:
    :return:
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            _random(p) if p.get('random') == 'true' else _all(p)
        ],
    )


def _all(p: dict) -> list:
    return [
        InlineKeyboardButton(
            text=answer.get('title'),
            callback_data=answer.get('paragraph_sha')
        )
        for answer in list(p.get('answers'))
    ]


def _random(p: dict) -> list:
    return [
        InlineKeyboardButton(
            text='  🎲  '.join(
                [
                    answer.get('title') for answer in p.get('answers')
                ]
            ),
            callback_data=random.choice(
                [
                    answer.get('paragraph_sha') for answer in p.get('answers')
                ]
            ),
        )
    ]
