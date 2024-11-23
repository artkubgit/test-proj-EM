from typing import Dict, Union


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.id = None  # ID будет установлен позже
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def to_dict(self) -> Dict[str, Union[int, str]]:
        """Конвертирует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict[str, Union[int, str]]) -> 'Book':
        """Создает объект книги из словаря."""
        book = Book(data['title'], data['author'], data['year'])
        book.id = data['id']
        book.status = data['status']
        return book