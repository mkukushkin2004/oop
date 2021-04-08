class Point:
    def __init__(self, x=0, y=0):  # конструктор
        print("создание экземпляра класса Point")
        self.x = x
        self.y = y


pt = Point(5)  # создаём экземпляр, при этом необязательный аргумент y = 0
print(pt.__dict__)
