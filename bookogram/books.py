import os
import sys
import yaml
import re
import hashlib
import bookogram.paragraph as Paragraph

BOOKS_DIR = '.'


def load_books(bindex: dict = {'books': {}, 'paragraphs': {}}, books_dir: str = BOOKS_DIR):
    for dirpath, dirnames, filenames in os.walk(books_dir):
        for filename in filenames:
            if re.search("bookogram\.ya?ml$", filename):
                filepath = f"{dirpath}/{filename}"

                print(filepath)

                with open(filepath, 'r') as file:
                    book = yaml.load(file, Loader=yaml.BaseLoader)

                    # print(f"book = {book}")

                    # TODO Тут должна быть проверка схемы
                    try:
                        book_id = f"{book.get('meta').get('title')} {book.get('meta').get('author')}"
                    except:
                        print(f"Не удалось прочитать книгу {filepath}: неправильная схема", file=sys.stderr)
                        continue

                    print(f"Прочитана книга {filepath} (book_id = \"{book_id}\")")

                    bindex['books'][book_id] = book.get('meta')

                    # Определение первого параграфа
                    entrance_id = f"{book_id} {book.get('paragraphs')[0].get('id')}"
                    entrance_sha = hashlib.sha3_256(entrance_id.encode()).hexdigest()

                    bindex['books'][book_id]['entrance_sha'] = entrance_sha

                    paragraphs = _paragraphs(book.get('paragraphs'), book_id)
                    print(f"    └ ├ paragraphs = {paragraphs}")

                    bindex['paragraphs'] = paragraphs

    return bindex


# Параграфы
def _paragraphs(paragraphs_list: list, book_id: str) -> dict:
    paragraphs = {}

    for paragraph_dict in paragraphs_list:
        paragraph = Paragraph.paragraph(paragraph_dict, book_id)
        print(f"  └ ├ paragraph = {paragraph}")

        paragraphs[paragraph.get('sha')] = paragraph

    return paragraphs
