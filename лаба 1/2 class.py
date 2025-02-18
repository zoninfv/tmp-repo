# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Box:
    def __init__(self, color: str | None, width: int | float, lenght: int | float):
        """Инициализация ящика

        :param color: Цвет ящика.
        :param width: Ширина ящика.
        :param lenght: Длина ящикаа.

        Примеры:
        >>> box = Box('Коричневый', 40, 80) # инициализация экземпляра класса
        >>> box = Box('Белый', 40, '80') # Неверная инициализация класса
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

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
