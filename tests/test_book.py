import unittest
from models.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.book = Book(title="Test Title", author="Test Author", year=2022)

    def test_initialization(self):
        """Проверка инициализации книги."""
        self.assertEqual(self.book.title, "Test Title")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.year, 2022)
        self.assertEqual(self.book.status, "в наличии")
        self.assertIsNone(self.book.id)

    def test_to_dict(self):
        """Проверка преобразования книги в словарь."""
        self.book.id = 1
        expected_dict = {
            "id": 1,
            "title": "Test Title",
            "author": "Test Author",
            "year": 2022,
            "status": "в наличии",
        }
        self.assertEqual(self.book.to_dict(), expected_dict)

    def test_from_dict(self):
        """Проверка создания книги из словаря."""
        book_data = {
            "id": 2,
            "title": "Another Title",
            "author": "Another Author",
            "year": 2021,
            "status": "выдана",
        }
        new_book = Book.from_dict(book_data)
        self.assertEqual(new_book.id, 2)
        self.assertEqual(new_book.title, "Another Title")
        self.assertEqual(new_book.author, "Another Author")
        self.assertEqual(new_book.year, 2021)
        self.assertEqual(new_book.status, "выдана")


if __name__ == "__main__":
    unittest.main()