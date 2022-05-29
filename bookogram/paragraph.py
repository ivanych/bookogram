import hashlib

import bookogram.answers as Answers


# Параграф
def paragraph(paragraph_dict: dict, book_id: str) -> dict:
    pid = f"{book_id} {paragraph_dict.get('id')}"
    sha = hashlib.sha3_256(pid.encode()).hexdigest()

    answers = Answers.answers(paragraph_dict.get('answers'), book_id)

    paragraph = {
        'book_id': book_id,
        'id': paragraph_dict.get('id'),
        'pid': pid,
        'sha': sha,
        'text': paragraph_dict.get('text'),
        'answers': answers,
        'random': paragraph_dict.get('random'),
    }

    print(f"  └ ├ paragraph = {paragraph}")

    return paragraph
