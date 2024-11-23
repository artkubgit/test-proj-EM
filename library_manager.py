from services.library import Library


def main():
    library = Library()

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти\n")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            library.add_book(title, author, year)
            print("Книга успешно добавлена!")
        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            if library.delete_book(book_id):
                print("Книга успешно удалена!")
            else:
                print("Книга с указанным ID не найдена.")
        elif choice == "3":
            key = input("Введите параметр для поиска (title, author, year): ").lower()
            value = input("Введите значение для поиска: ")
            results = library.search_books(key, value)
            if results:
                print("Найденные книги:")
                for book in results:
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги по заданным параметрам не найдены.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ").strip()
            if library.change_status(book_id, new_status):
                print("Статус книги успешно изменен!")
            else:
                print("Ошибка изменения статуса. Проверьте ID книги и новый статус.")
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
