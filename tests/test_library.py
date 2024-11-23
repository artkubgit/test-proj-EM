import unittest
from services.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library(storage_file="test_library.json")

    def tearDown(self):
        # Удаляем тестовый файл после завершения тестов
        import os
        if os.path.exists("test_library.json"):
            os.remove("test_library.json")

    def test_add_book(self):
        self.library.add_book("Test Book", "Author", 2022)
        self.assertEqual(len(self.library.books), 1)

    def test_delete_book(self):
        self.library.add_book("Test Book", "Author", 2022)
        book_id = self.library.books[0].id
        self.assertTrue(self.library.delete_book(book_id))
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        self.library.add_book("Python", "Guido", 1991)
        results = self.library.search_books("title", "python")
        self.assertEqual(len(results), 1)

    def test_change_status(self):
        self.library.add_book("Test Book", "Author", 2022)
        book_id = self.library.books[0].id
        self.assertTrue(self.library.change_status(book_id, "выдана"))
        self.assertEqual(self.library.books[0].status, "выдана")


if __name__ == "__main__":
    unittest.main()
