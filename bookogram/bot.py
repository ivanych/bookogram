from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from bookogram.books import books
from bookogram import paragraph

DELIMITER = '_'

dp = Dispatcher()


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
                    text=books.get(b).get("meta").get("title"),
                    # TODO нужно придумать как находить первый параграф в книге
                    callback_data=f"{b}{DELIMITER}Добро пожаловать!",
                )
                for b in books
            ],
        ],
    )

    text = f"Выберите книгу."

    await message.answer(text, reply_markup=ikm)


@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    b, p = callback.data.split(DELIMITER, 1)

    book = books.get(b)

    if book:
        paragraph_dict = book.get('paragraphs').get(p)

        if paragraph_dict:
            # TODO Хак с прицелом на дальнейшее использование классов
            # В параграфе должны быть данные о книге, в том числе идентификатор книги
            paragraph_dict['book_id'] = b

            p_vs = paragraph.variants(paragraph_dict)

            result = f"<b>{p} | {book.get('meta').get('title')}</b>\n" \
                     f"\n" \
                     f"{paragraph_dict.get('text')}";

            await callback.message.answer(result, reply_markup=p_vs)
        else:
            await callback.message.answer(f"⛔️️ Ошибка: параграф не найден.")
    else:
        await callback.message.answer(f"⛔️️ Ошибка: книга не найдена.")

    await callback.answer()
