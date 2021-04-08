class Point:
    def __init__(self, x=0, y=0):  # конструктор
        self.x = x
        self.y = y

    def __del__(self):  # деструктор, съедание объекта прописано в самом питоне, мы лишь добавляем функционал
        print("Удаление экземпляра: " + self.__str__())


pt = Point()
pt2 = Point(5)
pt3 = Point(5, 10)
pt2 = 0
del pt3
print('Goodbye')

