a, b = map(int, input().split())
try:
    if b == 0:
        raise ZeroDivisionError
except:
    print("Деление на 0")

print("Будет ли это напечатано?")
