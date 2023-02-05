class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self._name = name
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        self._author = author

    @property
    def name(self) -> str:  # при объявлении только getter - атрибут _name открыт только для чтения
        """getter не принимает аргумент, но возвращает название книги"""
        return self._name

    @property
    def author(self) -> str:  # при объявлении только getter - атрибут _author открыт только для чтения
        """getter не принимает аргумент, но возвращает название книги"""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Дочерний класс. Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть тпа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        """getter не принимает аргумент, но возвращает количество страниц в книге"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        """setter принимает и устанавливает новое количество страниц в книге"""
        if not isinstance(new_pages, int):
            raise TypeError("Новое количество страниц должно быть тпа int")
        if new_pages <= 0:
            raise ValueError("Новое количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    """Дочерний класс. Аудио книга"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудио должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность аудио должна быть типа положительным числом")
        self.duration = duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        """getter не принимает аргумент, но возвращает продолжительность аудиокниги"""
        return self._duration

    @duration.setter
    def duration(self, new_duration: int):
        """setter принимает и устанавливает новую продолжительность аудиокниги"""
        if not isinstance(new_duration, float):
            raise TypeError("Новая продолжительность аудиокниги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Новая продолжительность аудио должна быть типа положительным числом")
        self._duration = new_duration
