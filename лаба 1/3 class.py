# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Account:
    def __init__(self, username: None, phone: None):
        """"
        Инициализация записей аккаунтов соцсети.

        :param username: Имя пользователя.
        :param phone: Телефон абонента.
        """
        self.username = None
        self.phone = None
        self.record(username, phone)

    def record(self, username: str, phone: int)-> None:
        """
        Инициализирование атрибутов объекта.
        :param username: Имя.
        :param phone: Телефон

        >>> first = Accountbook('Alex', 9083601)
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        self.username = username
        if not isinstance(phone, int):
            raise TypeError("Телефон должен быть типа int")
        if 12 < len(str(phone)) < 7:
            raise ValueError("Телефон должен быть от 11 до 7 символов")
        self.phone = phone

    def clean(self):
        """
        Очистка записи

        >>> first = Account('Alex', 9083601)
        >>> first.clean()
        """
        self.username = None
        self.phone = None

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
