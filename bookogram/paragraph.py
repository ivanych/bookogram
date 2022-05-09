from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def variants(p: dict):
    """
    Метод формирует кнопки выбора вариантов

    :param p:
    :return:
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=variant_id,
                    callback_data=f"{p['book_id']}_{variant_id}"
                )
                for variant_id in list(p.get('answers'))
            ]
        ],
    )
