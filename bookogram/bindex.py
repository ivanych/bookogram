import os
import yaml
import re
import bookogram.meta as Meta
import bookogram.paragraphs as Paragraphs

BOOKS_DIR = '.'


def load_books(bindex: dict = {'books': {}, 'paragraphs': {}}, books_dir: str = BOOKS_DIR):
    for dirpath, dirnames, filenames in os.walk(books_dir):
        for filename in filenames:
            if re.search("bookogram\.ya?ml$", filename):
                filepath = f"{dirpath}/{filename}"

                print(filepath)

                with open(filepath, 'r') as file:
                    book = yaml.load(file, Loader=yaml.BaseLoader)

                    meta = Meta.meta(book.get('meta'), book.get('paragraphs'))
                    bindex['books'][meta.get('bid')] = meta

                    paragraphs = Paragraphs.paragraphs(book.get('paragraphs'), meta.get('bid'))
                    bindex['paragraphs'] = paragraphs

    return bindex
