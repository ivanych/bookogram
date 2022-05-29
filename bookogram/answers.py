import bookogram.answer as Answer


# Ответы
def answers(answers_list: list, book_id: str) -> list:
    answers = []

    for answer_dict in answers_list:
        answer = Answer.answer(answer_dict, book_id)

        answers.append(answer)

    print(f"└ ├ answers = {answers}")

    return answers
