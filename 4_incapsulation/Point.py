class Point:
    """
    Класс, описывающий точку на координатной плоскости от 0 до 100

    Все точки имеют ширину (__WIDTH) и высоту (__HEIGHT), равные 5px, их менять нельзя

    Каждая точка может иметь только 4 возможных атрибута:
    __x, __y - координаты точки - задаются для каждой точки при инициализации, могут быть изменены и получены
    доступ к координатом осуществляется посредством сеттера set_coords и геттера get_coords
    __color - её цвет - задаётся для каждой точки при инициализации, может быть изменён, но не может быть получен
    цвет можно поменять с помощью сеттера set_color
    name - имя точки - по умолчанию Anonymous, может быть перезадано свободно (public) (т.е. сеттеры и т.п. не надо)

    При инициализации объекта нужно проверять корректность координат (каждую отдельно) и цвета
    Координата корректна, если а) является числом и б) от 0 до 100
    Цвет корректен, если а) является строкой и б) длина строки <= 15
    Если корректно, ставим соответствующее свойство, иначе - бросаем исключение AttributeError
    Имя name - необязательный аргумент, по умолчанию name="Anonymous"

    Для проверки корректности координаты сделать статический приватный метод __is_correct_coord
    Дря проверки корректности цвета сделать статический приватный метод __is_correct_color

    Также реализовать public static method show_geometry, возвращающий кортежем __WIDTH и __HEIGHT

    Сделать деструктор __del__: при удалении объекта должен печататься текст "Точка с именем {name} удалена с плоскости"

    Перегрузить метод удаления атрибута __delattr__ так, чтобы атрибуты не удалялись, а печаталось, что нельзя удалять

    Перегрузить метод __getattribute__ так, чтобы нельзя было узнать цвет color (печатать, что цвет узнать нельзя,
    другие атрибуты узнавать можно, их возвращать)

    Перегрузить __getattr__ так, чтобы печаталось "атрибута {item} не существует"

    Сделать геттер get_coords (просто возвращает координаты __x и __y кортежем)

    Сделать сеттер set_coords, который проверяет корректность координат x и y, устанавливаемых пользователем
    Если оба корректны, ставим их, в ином случае - принтуем, что данные некорректны

    Аналогично сделать сеттер set_color

    Сделать статический метод show_geometry, дающий доступ к свойствам класса WIDTH и HEIGHT
    """

    __WIDTH = 5
    __HEIGHT = 5

    __slots__ = ["__x", "__y", "__color", "name"]

    @staticmethod
    def show_geometry():
        return Point.__WIDTH, Point.__HEIGHT

    @staticmethod
    def __is_correct_coord(coord):
        if not isinstance(coord, (int, float)):
            return False
        elif not 0 <= coord <= 100:
            return False
        return True

    @staticmethod
    def __is_correct_color(color):
        if not isinstance(color, str):
            return False
        elif not len(color) <= 15:
            return False
        return True

    def __init__(self, x: int, y: int, color: str, name="Anonymous"):
        self.name = name
        if Point.__is_correct_coord(x):
            self.__x = x
        else:
            raise AttributeError("Некорректное значение координаты x")
        if Point.__is_correct_coord(y):
            self.__y = y
        else:
            raise AttributeError("Некорректное значение координаты y")
        if Point.__is_correct_color(color):
            self.__color = color
        else:
            raise AttributeError("Некорректное значение цвета точки")

    def __del__(self):
        print(f"Точка {self.name} с координатами {self.__x, self.__y} удалена с плоскости")

    def __delattr__(self, item):
        print(f"Извините, но атрибут {item} не может быть удалён!")

    def __getattribute__(self, item):
        if item == "color":
            print("Цвет узнавать нельзя!")
            return
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print(f"Атрибута {item} не существует!")

    def set_coords(self, x: int, y: int):
        if Point.__is_correct_coord(x) and Point.__is_correct_coord(y):
            self.__x = x
            self.__y = y
        else:
            print("Координата должна быть целым или вещественным числом от 0 до 100!")

    def get_coords(self):
        return self.__x, self.__y

    def set_color(self, color):
        if Point.__is_correct_color(color):
            self.__color = color
        else:
            print("Цвет должен быть строкой длиной не более 15!")
