from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from bookogram.book import book

dp = Dispatcher()


def start(bot_token: str) -> None:
    # Initialize Bot instance with an default parse mode which will be passed to all API calls
    bot = Bot(bot_token, parse_mode="HTML")

    # And the run events dispatching
    dp.run_polling(bot)


@dp.message(commands=["start"])
async def command_book_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='001', callback_data='001'),
                InlineKeyboardButton(text='002', callback_data='002')
            ]
        ],
    )

    await message.answer(f"Книга", reply_markup=ikm)


@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    p = book.get(callback.data)

    if p:
        ikm = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=answer, callback_data=answer) for answer in p.get('answers')
                ]
            ],
        )

        await callback.message.answer(f"<b>{p.get('num')}</b>\n\n{p.get('text')}", reply_markup=ikm)
    else:
        await callback.message.answer(f"⛔️️ Этот параграф пока не готов.")

    await callback.answer()
