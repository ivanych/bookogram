import random
import hashlib
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import bookogram.answer as Answer


# Параграф
def paragraph(paragraph_dict: dict, book_id: str) -> dict:
    pid = f"{book_id} {paragraph_dict.get('id')}"
    sha = hashlib.sha3_256(pid.encode()).hexdigest()

    answers = _answers(paragraph_dict.get('answers'), book_id)
    print(f"└ ├ answers = {answers}")

    paragraph = {
        'book_id': book_id,
        'id': paragraph_dict.get('id'),
        'pid': pid,
        'sha': sha,
        'text': paragraph_dict.get('text'),
        'answers': answers,
        'random': paragraph_dict.get('random'),
    }

    return paragraph


# Ответы
def _answers(answers_list: list, book_id: str) -> list:
    answers = []

    for answer_dict in answers_list:
        answer = Answer.answer(answer_dict, book_id)
        print(f"├ answer = {answer}")

        answers.append(answer)

    return answers


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
