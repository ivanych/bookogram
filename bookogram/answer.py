import hashlib


# Ответ
def answer(answer_dict: dict, book_id: str) -> dict:
    paragraph_pid = f"{book_id} {answer_dict.get('id')}"
    paragraph_sha = hashlib.sha3_256(paragraph_pid.encode()).hexdigest()

    answer = {
        'paragraph_id': answer_dict.get('id'),
        'paragraph_pid': paragraph_pid,
        'paragraph_sha': paragraph_sha,
        'title': answer_dict.get('title'),
    }

    return answer
