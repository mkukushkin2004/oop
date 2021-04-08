class Point:
    x = 1
    y = 1

    def set_coords(self, x, y):
        self.a = x  # через self создаём локальные атрибуты
        self.b = y  # они принадлежат только экземпляру класса


pt = Point()
pt2 = Point()
pt.set_coords(5, 10)  # вызываем метод для одного экземпляра класса
pt2.set_coords(2, 3)  # и для другого
print(pt.__dict__)  # благодаря self метод "опознал" нужный экземпляр
print(pt2.__dict__)  # и изменил только его, экземпляра, атрибуты

pt.set_coords(5, 10)  # эта строчка
Point.set_coords(pt, 5, 10)  # эквивалентна этой
