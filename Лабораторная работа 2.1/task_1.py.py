# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Сube:
    def __init__(self, weight: float, len: float):
        """
        Создание и подготовка к работе объекта "Куб"
        :param len: Длина ребра куба в см
        :param weight: Вес куба
        Примеры:
        >>> cube = Сube(20, 50)  # инициализация экземпляра класса
        """
        if not isinstance(len, (int, float)):
            raise TypeError("Длина ребра куба должна быть типа int или float")
        if len <= 0:
            raise ValueError("Длина ребра куба должа быть положительным числом")
        self.len = len

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть int или float")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self.weight = weight

    def cube_volume(self):
        """
        Функция которая считает объем куба
        :return: Объем куба
        Примеры:
        >>> cube = Сube(20, 50)
        >>> cube.cube_volume()
        """
        return self.len**3

    def cube_density(self):
        """
        Расчет плотности куба.
        :return: Плотность куба
        Примеры:
        >>> cube = Сube(20, 50)
        >>> cube.cube_density
        """
        return self.weight * self.cube_volume()

figure = Сube(30, 20)

print(figure.cube_volume())
print(figure.cube_density())

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass




class Basket:
    def __init__(self, apple: int, pear: int):
        """
        Создание и подготовка к работе объекта "Корзина"
        :param apple: Количество яблок в корзине
        :param pear: Количество груш в корзине
        Примеры:
        >>> basket = Basket(20, 50)  # инициализация экземпляра класса
        """
        if not isinstance(apple, int):
            raise TypeError("Количество яблок должно быть типа int")
        if apple < 0:
            raise ValueError("Количество яблок должно быть не отрицательным числом")
        self.apple = apple

        if not isinstance(pear, int):
            raise TypeError("Количество груш должно int")
        if pear < 0:
            raise ValueError("Количество груш должно быть не отрицательным числом")
        self.pear = pear

    def is_empty_basket(self) -> bool:
        """
        Функция которая проверяет является ли корзина пустой
        :return: Является ли корзина пустой
        Примеры:
        >>> basket = Basket(20, 0)
        >>> basket.is_empty_basket()
        """
        if self.pear == 0 and self.apple == 0:
            return True
        else:
            return False


    def total_fruit(self):
        """
        Подсчет фруктов в корзине.
        :return: Количество фруктов
        Примеры:
        >>> basket = Basket(20, 50)
        >>> basket.total_fruit
        """
        return self.apple + self.pear

bask_ = Basket(0, 0)

print(bask_.is_empty_basket())
print(bask_.total_fruit())





class BankAccount:
    def __init__(self, money: float, expenses: float):
        """
        Создание и подготовка к работе объекта "Карта"
        :param money: Баланс на карте
        :param expenses: Расходы
        Примеры:
        >>> Bank = BankAccount(60, 50)  # инициализация экземпляра класса
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Баланс должен быть типа int или float")
        if money < 0:
            raise ValueError("Баланс должен быть не отрицательным числом")
        self.money = money

        if not isinstance(expenses, (int, float)):
            raise TypeError("Расходы должны быть типа int или float")
        if expenses < 0:
            raise ValueError("Расходы должны быть не отрицательным числом")
        self.expenses = expenses
        if self.expenses > self.money:
            raise ValueError("Расходы должны быть меньше баланса")

    def add_money_to_the_account(self, add_money: float):
        """
        Добавление денег на счет.
        :param add_money: Добавляемая сумма
        Примеры:
        >>> Bank = BankAccount(60, 50)
        >>> Bank.add_money_to_the_account(10)
        """
        if not isinstance(add_money, (int, float)):
            raise TypeError("Добавляемая сумма должна быть типа int или float")
        if add_money < 0:
            raise ValueError("Добавляемая сумма должна быть положительным числом")

        self.money += add_money
        return self.money

    def account_balance(self):
        """
        Подсчет остатка на счете.
        :return: Остаток на счете
        Примеры:
        >>> Bank = BankAccount(60, 50)
        >>> Bank.account_balance
        """
        return self.money - self.expenses

bank = BankAccount(60, 50)

print(bank.add_money_to_the_account(10))
print(bank.account_balance())