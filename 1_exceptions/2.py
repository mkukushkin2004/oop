try:
    print('10'+10)
    print('1')
except (TypeError, ZeroDivisionError):  # сразу несколько исключений
    print("Неверный ввод")
