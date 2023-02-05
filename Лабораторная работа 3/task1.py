class Write_Author_Error(Exception):
    pass

class Write_Name_Error(Exception):
    pass

class Book:
    def __init__(self, name: str, author: str):
        self._author = author
        self._name = name

    def __str__(self):
        return f"Book's name is '{self._name}' and written by {self._author}'"

    def __repr__(self):
        return repr(f'{self._name} {self._author}')

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        raise Write_Author_Error("Author can't be changed")

    @name.setter
    def name(self, value):
        raise Write_Name_Error("Name can't be changed")


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float) or duration < 0:
            raise ValueError("Duration must be float and >= 0")
        self._duration = duration

    def __repr__(self):
        return repr(f'{self._name} {self._author} {self._duration}')

    @property
    def duration(self):
        print("Getting value...")
        return self._duration

    @duration.setter
    def duration(self, value):
        print("Setting duration value")
        if not isinstance(value, float) or value < 0:
            raise ValueError("Duration must be float and >= 0")
        self._duration = value


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Pages must be integer and >= 0")
        self._pages = pages

    def __repr__(self):
        return repr(f'{self._name} {self._author} {self._pages}')

    @property
    def pages(self):
        print("Getting value...")
        return self._pages

    @pages.setter
    def pages(self, value):
        print("Setting pages value")
        if not isinstance(value, int) or value < 0:
            raise ValueError("Pages must be integer and >= 0")
        self._pages = value


if __name__ == "__main__":
    pass
    # b = Book("Мастер и Маргарита", "Булгаков")
    # print(b.author)
    # print(b.name)
    # ab = AudioBook("Мастер и Маргарита", "Булгаков, 120.1)
    # ab.duration = -10.12
    # pb = PaperBook("Мастер и Маргарита", "Булгаков, -10)
