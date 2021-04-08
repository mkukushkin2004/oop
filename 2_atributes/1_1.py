class Point:
    """Класс для представления координат точек на плоскости"""
    x = 0
    y = 0
    z = 0


print(Point.__doc__)
print(Point.__name__)
print(dir(Point))

print(type(Point))

pt = Point()  # экземпляр класса
print(type(pt))

print(pt.x)   # обращение к свойству

Point.x = 100
print(pt.x)
pt.x = 5
print(pt.x, Point.x)

print(id(pt), id(Point))
print(pt.y)
pt.color = 'red'
print(pt.__dict__)

print(getattr(Point, 'x'))  # узнать значение атрибута класса или объекта
print(getattr(pt, '', None))

print(hasattr(pt, 'z'))

setattr(pt, 'z', 100)
print(pt.__dict__)

pt.z = 100

delattr(Point, 'z')

# эти функции дают большую гибкость при работе с атрибутами

print(isinstance(pt, (list, Point)))
