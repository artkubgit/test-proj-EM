import json
from models.book import Book
from typing import List


class Library:
    def __init__(self, storage_file: str = "data/library.json"):
        self.storage_file = storage_file
        self.books: List[Book] = []
        self.load_books()

    def load_books(self) -> None:
        """Загрузка данных из файла."""
        try:
            with open(self.storage_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book_data) for book_data in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self) -> None:
        """Сохранение данных в файл."""
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавление книги в библиотеку."""
        new_book = Book(title, author, year)
        new_book.id = max((book.id for book in self.books), default=0) + 1
        self.books.append(new_book)
        self.save_books()

    def delete_book(self, book_id: int) -> bool:
        """Удаление книги по ID."""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return True
        return False

    def search_books(self, key: str, value: str) -> List[Book]:
        """Поиск книг по названию, автору или году."""
        return [
            book for book in self.books
            if value.lower() in str(getattr(book, key, "")).lower()
        ]

    def change_status(self, book_id: int, new_status: str) -> bool:
        """Изменение статуса книги."""
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    return True
        return False

    def display_books(self) -> None:
        """Отображение всех книг в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
        else:
            print(f"{'ID':<5} {'Название':<30} {'Автор':<20} {'Год':<6} {'Статус':<10}")
            print("-" * 80)
            for book in self.books:
                print(f"{book.id:<5} {book.title:<30} {book.author:<20} {book.year:<6} {book.status:<10}")
