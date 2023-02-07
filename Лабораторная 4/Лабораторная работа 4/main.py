class Sport:
    """ Базовый класс "Спорт" """

    def __init__(self, name: str, level: str):
        """
        Подготовка объекта "Спорт"
        :param name: Наименование спорта
        :param level: Уровень физической подготовки: "начальный", "средний" или "продвинутый"
        Уровни постоянны и заданны в виде защищенного атрибута.

        Параметр category: Спортивный разряд - по умолчанию None.
        Задается через метод get_sport_category, только при наличии уровня "продвинутый"

        Пример:
        >>> dance = Sport("Танцы", "начальный")
        """

        if not isinstance(name, str):
            raise TypeError("Наименование спорта должно быть типа str")
        self.name = name

        self._FITNESS_LEVEL = ["начальный", "средний", "продвинутый"]
        if not isinstance(level, str):
            raise TypeError("Уровень физической подготовки должен быть типа str")
        if level in self._FITNESS_LEVEL:
            self.level = level
        else:
            raise ValueError("Уровень подготовки должен быть: начальный, средний или продвинутый")

        self._category = None  # для метода get_sport_category
        self._hundred_meter_run = None  # для метода level_indicator
        self._jump_length = None  # для метода level_indicator
        self._press = None  # для метода level_indicator

    def __str__(self) -> str:
        """
        Метод для нестрогово представления экземпляра класса.
        Метод наследуется в классе Skiing и Gymnastics

        Пример:
        >>> dance = Sport("Танцы", "начальный")
        >>> dance.__str__()
        'Спорт: Танцы. Уровень подготовки: начальный.'
        """
        return f"Спорт: {self.name}. Уровень подготовки: {self.level}."

    def __repr__(self) -> str:
        """
        Метод для вывода валидного Python кода

        Пример:
        >>> dance = Sport("Танцы", "начальный")
        >>> dance.__repr__()
        "Sport(name='Танцы', level='начальный')"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, level={self.level!r})"

    def get_sport_category(self, category: str) -> None:
        """
        Метод для фиксирования достигнутого спортивного разряда
        :param category: Спортивный разряд.
        Спортивный разряд дается только при наличии уровня "продвинутый"

        Пример:
        >>> dance = Sport("Танцы", "продвинутый")
        >>> dance.get_sport_category("Кандидат в мастера спорта")
        """
        if not isinstance(category, str):
            raise TypeError("Спортивный разряд должен быть типа str")
        if self.level == self._FITNESS_LEVEL[-1]:
            self._category = category
        else:
            raise ValueError("Спортивный разряд дается только при наличии уровня продвинутый")

    def level_indicator(self, hundred_meter_run: float, jump_length: float, press: int) -> None:
        """
        Метод для фиксации личных показателей в виде нормативов общей физической подготовки.
        Показатели меняются в зависимости от направления спорта.
        :param hundred_meter_run: Время преодоления дистанции на 100 метров, сек
        :param jump_length: Прыжок в длину с места, метры
        :param press: Количество подъемов туловища в положении лежа, раз

        >>> dance = Sport("Танцы", "продвинутый")
        >>> dance.level_indicator(15.35, 1.76, 56)
        """
        if not isinstance(hundred_meter_run, float):
            raise TypeError
        if hundred_meter_run <= 0:
            raise ValueError
        self._hundred_meter_run = hundred_meter_run

        if not isinstance(jump_length, float):
            raise TypeError
        if jump_length <= 0:
            raise ValueError
        self._jump_length = jump_length

        if not isinstance(press, int):
            raise TypeError
        if press <= 0:
            raise ValueError
        self._press = press


class Skiing(Sport):
    """ Дочерний класс "Горнолыжный спорт" """

    def __init__(self, name: str, level: str, style: str):
        """
        Подготовка объекта "Горнолыжный спорт"
        :param name: Наименование спорта
        :param level: Уровень подготовки
        :param style: Направление

        Пример:
        >>> snowboard = Skiing("Сноуборд", "начальный", "фрирайд")
        """
        super().__init__(name, level)
        self.style = style

        self._distance = None  # для метода level_indicator
        self._time = None  # для метода level_indicator

    def __repr__(self) -> str:
        """
        Метод для вывода валидного Python кода.
        Метод перезаписывается, так как в классе Skiing задается новый атрибут: style

        Пример:
        >>> snowboard = Skiing("Сноуборд", "начальный", "фрирайд")
        >>> snowboard.__repr__()
        "Skiing(name='Сноуборд', level='начальный', style='фрирайд')"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, level={self.level!r}, style={self.style!r})"

    def level_indicator(self, distance: int, time: float) -> None:
        """
        Метод для фиксации личных показателей в виде времени преодолеия и дистанции
        :param distance: Дистанция, метры
        :param time: Время преодоления дистанции, сек

        Пример:
        >>> snowboard = Skiing("Сноуборд", "начальный", "фрирайд")
        >>> snowboard.level_indicator(750, 56.17)
        """
        if not isinstance(distance, int):
            raise TypeError("Дистанция должна быть типа int")
        if distance <= 0:
            raise ValueError("Дистанция должна быть положительным числом")
        self._distance = distance

        if not isinstance(time, float):
            raise TypeError("Время преодоления дистанции должно быть типа float")
        if time <= 0:
            raise ValueError("Время преодоления дистанции должно быть положительным числом")
        self._time = time


class Gymnastics(Sport):
    """ Дочерний класс "Гимнастика" """

    def __init__(self, name: str, level: str, inventory: str):
        """
        Подготовка объекта "Гимнастика"
        :param name: Наименование спорта
        :param level: Уровень подготовки
        :param inventory: Спортивный инвентарь

        Пример:
        >>> artistic_gymnastics = Gymnastics("Художественная гимнастика", "продвинутый", "булавы")
        """
        super().__init__(name, level)
        self.inventory = inventory

        self._score = None  # для метода level_indicator

    def __repr__(self) -> str:
        """
        Метод для вывода валидного Python кода.
        Метод перезаписывается, так как в классе Gymnastics задается новый атрибут: inventory

        Пример:
        >>> artistic_gymnastics = Gymnastics("Художественная гимнастика", "продвинутый", "булавы")
        >>> artistic_gymnastics.__repr__()
        "Gymnastics(name='Художественная гимнастика', level='продвинутый', inventory='булавы')"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, level={self.level!r}, inventory={self.inventory!r})"

    def level_indicator(self, score: int) -> None:
        """
        Метод для фиксации личных показателей в виде количества баллов за выступление
        :param score: Количество баллов

        Пример:
        >>> artistic_gymnastics = Gymnastics("Художественная гимнастика", "продвинутый", "булавы")
        >>> artistic_gymnastics.level_indicator(54)
        """

        if not isinstance(score, int):
            raise TypeError("Количество баллов должно быть типа int")
        if score <= 0:
            raise ValueError("Количество баллов должно быть положительным числом")
        self._score = score


if __name__ == "__main__":
    pass
