# хотим оставить функционал геттеров, сеттеров и делиттеров, но делать это как раньше, "напрямую"
# чем отличается новый метод?"
# теперь можно вызвать без скобок и он прикидывается обычной переменной-членом класса,
# хотя внутри может быть спрятана весьма замысловатая логика. Обычный геттер, сеттер, делитер, только более удобный.
# более того, мы объединяем геттер, сеттер и делитер в одно "свойство"

class Point:
    def __init__(self, x=0):
        self.__x = x

    def get_coord(self):
        print("Получение свойства")
        return self.__x

    def set_coord(self, value):
        print("Установка свойства")
        self.__x = value

    def del_coord(self):
        print("Удаление свойства")
        del self.__x

    coord_x = property(get_coord, set_coord, del_coord, "I'm the 'x' property")


pt = Point()
print(pt.x)
pt.x = 5
print(pt.x)
del pt.x
