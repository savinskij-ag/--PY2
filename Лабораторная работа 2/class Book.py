class Book:
    """
    Class represents Book entity
    """

    def __init__(self, id_, name, pages):
        self.pages = pages
        self.name = name
        self.id = id_

    def __str__(self) -> str:
        return f"Книга \"{self.name}\""

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})"

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=BOOKS_DATABASE["id"], name=BOOKS_DATABASE["name"], pages=BOOKS_DATABASE["pages"]) for BOOKS_DATABASE in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
