import hashlib


# Мета
def meta(meta_dict: dict, paragraphs_list: list) -> dict:
    bid = f"{meta_dict.get('title')} {meta_dict.get('author')}"

    # Определение первого параграфа
    entrance_pid = f"{bid} {paragraphs_list[0].get('id')}"
    entrance_sha = hashlib.sha3_256(entrance_pid.encode()).hexdigest()

    meta = {
        'bid': bid,
        'title': meta_dict.get('title'),
        'author': meta_dict.get('author'),
        'entrance_pid': entrance_pid,
        'entrance_sha': entrance_sha,
    }

    print(f"├ meta = {meta}")

    return meta
