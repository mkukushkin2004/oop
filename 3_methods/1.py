class Point:
    x = 1
    y = 1

    def set_coords(self):  # метод - общий для всех экземпляров
        print(self.__dict__)  # self - ссылка на конкретный экземпляр класса


pt = Point()
pt.x = 5
pt.y = 10
pt.set_coords()  # Python автоматически пробрасывает self при вызове метода

