import doctest


class Calendar:
    def __init__(self, day: int, month: int, year: int, event: str):
        """
        Создание и подготовка к работе объекта "Календарь"

        :param day: День месяца (число)
        :param month: Месяц (число)
        :param year: Год (число)
        :param event: Событие (по умолчанию None)

        Пример:
        >>> calendar = Calendar(22, 1, 2023, "Дедлайн по Лаб1")
        """

        if not isinstance(day, int):
            raise TypeError("День месяца должен быть типа int")
        self.day = day

        if not isinstance(month, int):
            raise TypeError("Месяц должен быть типа int")
        if month > 12:
            raise ValueError("В году 12 месяцев")
        self.month = month

        if not isinstance(year, int):
            raise TypeError("Год должен быть типа int")
        self.year = year

        self.event = None
        self.init_event(event)

    def init_event(self, event) -> None:
        if not isinstance(event, str):
            raise TypeError("Событие должно быть типа str")
        self.event = event

    def day_of_the_week(self) -> str:
        """
        Функция, которая определяет день недели

        :return: День недели

        Пример:
        >>> calendar = Calendar(22, 1, 2023, "Дедлайн по Лаб1")
        >>> calendar.day_of_the_week()
        """
        ...

    def is_things_planned(self) -> bool:
        """
        Функция, которая определяет, есть ли запланированные дела

        :return: Наличие планов

        Пример:
        >>> calendar = Calendar(22, 1, 2023, "Дедлайн по Лаб1")
        >>> calendar.is_things_planned()
        """
        ...


class Triangle:
    def __init__(self, side_a: int, side_b: int, side_c: int):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param side_a: Сторона треуголника - a
        :param side_b: Сторона треуголника - b
        :param side_c: Сторона треуголника - c

        Пример:
        >>> triangle = Triangle(12, 12, 12)
        """

        if not isinstance(side_a, int):
            raise TypeError("Сторона 'a' треугольника должна быть типа int")
        if side_a <= 0:
            raise ValueError("Сторона 'a' треугольника должна быть положительным числом")
        self.side_a = side_a

        if not isinstance(side_b, int):
            raise TypeError("Сторона 'b' треугольника должна быть типа int")
        if side_b <= 0:
            raise ValueError("Сторона 'b' треугольника должна быть положительным числом")
        self.side_b = side_b

        if not isinstance(side_c, int):
            raise TypeError("Сторона 'c' треугольника должна быть типа int")
        if side_c <= 0:
            raise ValueError("Сторона 'c' треугольника должна быть положительным числом")
        self.side_c = side_c

        if side_a + side_b < side_c or side_a + side_c < side_b or side_c + side_b < side_a:
            raise ValueError("Треугольник с данными сторонами не существует")

    def perimetr(self) -> int:
        """
        Функция, которая вычисляет периметр треугольника

        :return: Периметр треугольника

        Пример:
        >>> triangle = Triangle(12, 12, 12)
        >>> triangle.perimetr()
        36
        """
        return self.side_a + self.side_b + self.side_c

    def area(self) -> int:
        """
        Функция, которая вычисляет площадь треугольника

        :return: Площадь треугольника

        Пример:
        >>> triangle = Triangle(12, 12, 12)
        >>> triangle.area()
        """
        ...


class Car:
    def __init__(self, doors: int, wheels: int, mileage: int, gas_tank: int, fuel_volume: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param doors: Количество дверей
        :param wheels: Количество колес
        :param mileage: Пробег
        :param gas_tank: Объем топливного бака
        :param fuel_volume: Объем топлива

        Пример:
        >>> bmw = Car(5, 4, 10000, 70, 56)
        """

        if not isinstance(doors, int):
            raise TypeError("Количество дверей должно быть типа int")
        if doors < 0:
            raise ValueError("Количество дверей не может быть отрицательным")
        self.doors = doors

        if not isinstance(wheels, int):
            raise TypeError("Количество колес должно быть типа int")
        if wheels < 0:
            raise ValueError("Количество колес не может быть отрицательным")
        self.wheels = wheels

        if not isinstance(mileage, int):
            raise TypeError("Пробег должен быть типа int")
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным")
        self.mileage = mileage

        if not isinstance(gas_tank, int):
            raise TypeError("Объем топливного бака должен быть типа int")
        if gas_tank <= 0:
            raise ValueError("Объем топливного бака должен быть положительным числом")
        self.gas_tank = gas_tank

        if not isinstance(fuel_volume, int):
            raise TypeError("Объем топлива должен быть типа int")
        if fuel_volume < 0:
            raise ValueError("Объем топлива не может быть отрицательным")
        self.fuel_volume = fuel_volume

    def start_the_engine(self) -> str:
        """
        Функция, которая заводит двигатель автомобиля

        :return: Запустился ли двигатель

        Пример:
        >>> bmw = Car(5, 4, 10000, 70, 56)
        >>> bmw.start_the_engine()
        'Двигатель запущен'
        """
        if self.fuel_volume > 0:
            return "Двигатель запущен"
        else:
            return "Недостаточно бензина для запуска двигателя"

    def is_empty_tank(self) -> bool:
        """
        Функция, которая определяет наличие топлива в баке

        :return: Является ли бак пустым

        Пример:
        >>> bmw = Car(5, 4, 10000, 70, 16)
        >>> bmw.is_empty_tank()
        """

    def refill_the_tank(self, fuel: int) -> None:
        """
        Пополняем топливо

        :param fuel: Объем пополняемого топлива
        :raise ValueError: Если количество пополняемого топлива превышает свободное место в баке, то вызываем ошибку

        Пример:
        >>> bmw = Car(5, 4, 10000, 70, 16)
        >>> bmw.refill_the_tank(30)
        """
        if not isinstance(fuel, int):
            raise TypeError("Объем пополняемого топлива должен быть типа int")
        if fuel < 0:
            raise ValueError("Добавляемое топливо должно быть положительным числом")
        if self.fuel_volume + fuel > self.gas_tank:
            raise ValueError("Слишком много топлива")
        self.fuel_volume += fuel


if __name__ == "__main__":
    doctest.testmod()  # Проверка работоспособности экземпляров класса с помощью doctest
    pass
