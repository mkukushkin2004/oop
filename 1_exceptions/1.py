a, b = 1, 0
try:
    print(a / b)
except ZeroDivisionError:
    print("Делить на 0 нельзя!")
print("Будет ли это напечатано?")
