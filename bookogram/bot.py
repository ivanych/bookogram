import random
from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from bookogram import bindex as Bindex, paragraph as Paragraph

DELIMITER = '_'

dp = Dispatcher()

bindex = Bindex.load_books()


def start(bot_token: str) -> None:
    # Initialize Bot instance with an default parse mode which will be passed to all API calls
    bot = Bot(bot_token, parse_mode="HTML")

    # And the run events dispatching
    dp.run_polling(bot)


@dp.message(commands=["start"])
async def command_book_handler(message: Message) -> None:
    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=bindex.get('books').get(bid).get("title"),
                    callback_data=bindex.get('books').get(bid).get("entrance_sha"),
                )
                for bid in bindex.get('books')
            ],
        ],
    )

    text = f"Выберите книгу."

    await message.answer(text, reply_markup=ikm)


@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    paragraph = bindex.get('paragraphs').get(callback.data)

    if paragraph:
        ikm = _answers_ikm(paragraph)

        result = f"<b>{paragraph.get('id')} | {bindex.get('books').get(paragraph.get('book_id')).get('title')}</b>\n" \
                 f"\n" \
                 f"{paragraph.get('text')}";

        await callback.message.answer(result, reply_markup=ikm)
    else:
        await callback.message.answer(f"⛔️️ Ошибка: параграф не найден.")

    await callback.answer()


def _answers_ikm(p: dict) -> InlineKeyboardMarkup:
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
