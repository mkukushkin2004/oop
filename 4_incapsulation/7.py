# как уберечь объекты от появления лишних свойств?

class Point:
    WIDTH = 100
    __slots__ = ['__x', '__y']  # теперь у объектов могут быть заданы только такие атрибуты
    # проставить сюда WIDTH нельзя :)
    # также важно, что если вы используете __slots__, нельзя использовать __dict__!


pt = Point()
print(pt.z)

