import bookogram.paragraph as Paragraph


# Параграфы
def paragraphs(paragraphs_list: list, book_id: str) -> dict:
    paragraphs = {}

    for paragraph_dict in paragraphs_list:
        paragraph = Paragraph.paragraph(paragraph_dict, book_id)

        paragraphs[paragraph.get('sha')] = paragraph

    return paragraphs
