import yaml

# TODO Нужно сделать чтение из всех имеющихся файлов

file_path = 'books/books.yml'

with open(file_path, 'r') as file:
    books = yaml.load(file, Loader=yaml.BaseLoader)
