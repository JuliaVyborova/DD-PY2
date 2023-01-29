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


# Написание класса Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге

        Пример:
        book_1 = Book(1, "Название книги", 700)
        """

        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")
        self.pages = pages


# Написание класса Library
class Library:
    def __init__(self, books=None):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: Список книг

        Пример:
        my_library = Library()  #инициализация пустой библиотеки
        """

        if books is None:
            books = []
        if not isinstance(books, list):
            raise TypeError("Список книг должен быть типа list")
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, который возвращает идентификатор для добавления новой книги в библиотеку

        :return: Если книг в библиотеке нет, то возвращается 1.
        Если книги есть, то возвращается идентификатор последней книги увеличенный на 1.

        Пример:
        my_library = Library()
        my_library.get_next_book_id()
        1
        """

        return 1 if self.books == [] else len(self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод, который возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса.
        :param book_id: Запрашиваемый id книги
        :return: Если книга существует, то возвращается индекс из списка. Если книги нет, то вызывается ошибка
        """

        if not isinstance(book_id, int):
            raise TypeError("Запрашиваемый id книги должен быть типа int")
        if book_id <= 0:
            raise ValueError("Запрашиваемый id книги должен положительным числом")

        for index, book_in_library in enumerate(self.books):  # проходимся по индексам книг в библиотеке
            if book_id == book_in_library.id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
