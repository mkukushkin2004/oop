from Point import Point

p1 = Point(5, 10, "red")  # создаю объект
p1.name = "Ben"  # имя меняю без проблем, что хочу, то и ворочу

delattr(p1, 'name')  # удаление атрибута не проходит
del p1  # удаление точки

try:
    pt2 = Point(-1, -1, "red")  # пытаемся создать некорректную точку
except AttributeError:
    print("Не удалось создать точку! Неверные входные данные!")
# так как в процессе создания объекта Point произошло исключение, создание ссылки pt2 не произошло и объект удалён


pt3 = Point(2, 100, "black", "Vanya")
pt3.set_coords(1, 100)  # задаём координаты, всё норм
pt3.set_coords(-1, 100)  # а здесь не норм

print(pt3.get_coords())

print(Point.show_geometry())
print(pt3.show_geometry())
Point.__WIDTH = 1
print(Point.show_geometry())