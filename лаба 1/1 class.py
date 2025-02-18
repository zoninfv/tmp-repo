# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Car:
    def __init__(self, color: str, height: int | float):
        """Инициализация стула

        :param color: Цвет авто.
        :param height: Клиренс авто.

        Примеры:
        >>> car = Car('Белый', 13) # инициализация экземпляра класса
        >>> car = Car ('Белый', '25') # Неверная инициализация класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        if not isinstance(height, (int, float)):
            raise TypeError("Клиренс машины должен быть типа int или float")
        if float(1) < height < float(10) or height > float(22):
            raise ValueError("Клиренс слишком мал или велик")
        self.color = color
        self.height = height

    def set_color(self, color: str) -> None:
        """
        Изменение цвета авто.

        :param color: Задаваемый цвет.

        Пример:
        >>> car = Car('Белый', 13)
        >>> car.set_color('Черный')
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color =color

    def set_height(self, height: int | float) -> None:
            """
            Изменение клиренса.

            :param height: Выбираемый клиренс.

            Пример:
            >>> car = Car(13)
            >>> car.set_height(30)
            """
            if not isinstance(height, (int, float)):
                raise TypeError("Значение должен быть типа int или float")
            if float(1) < height < float(10) or height > float(22):
                raise ValueError("Клиренс легкового автомобиля не бывает таким")
            self.height = height

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


class Box:
    def __init__(self, color: str | None, width: int | float, lenght: int | float):
        """Инициализация стола

        :param color: Цвет ящика.
        :param width: Ширина ящика.
        :param lenght: Длина ящикаа.

        Примеры:
        >>> box = Table('Коричневый', 40, 80) # инициализация экземпляра класса
        >>> table = Table('Белый', 40, '80') # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        TypeError: Ширина и длина ящика должен быть типа int или float
        """

        if not (isinstance(width, (int, float)) and isinstance(lenght, (int, float))):
            raise TypeError("Ширина и длина ящика должны быть типа int или float")
        if width < float(20):
            raise ValueError("Слишком узкий ящик. Рекомендуется от 20 см")
        if lenght < float(40):
            raise ValueError("Слишком короткий ящик. Рекомендуется от 40 см")

        self.color = None
        self.init_color(color)
        self.width = width
        self.lenght = lenght

    def init_color(self, color: str) -> None:
        """
        Инициализация цвета ящика.

        :param color: Задаваемый цвет.

        Пример:
        >>> box = Box(color=None, width=30, lenght=60)
        >>> box.init_color('Черный')
        """
        if not isinstance(color, str|None):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

    def quadratic(self) -> bool:
        """
        Проверка является ли ящик квадратным.

        :return:  Является ли ящик квадратным

        >>> box = Box(None, 40, 40)
        >>> box.quadratic()
        True
        """
        if self.width == self.lenght:
            return True
        else:
            return False