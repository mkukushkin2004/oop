a, b = map(int, input().split())
if b == 0:
    raise ZeroDivisionError("Нельзя делить на ноль!!!! ТЫ дурак!!!")
else:
    print(a / b)
