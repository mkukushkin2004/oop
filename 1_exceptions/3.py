try:
    print(1 + 2)
    print(1 / 0)
except NameError:
    print("summa не существует")
except ZeroDivisionError:
    print("делить на 0 нельзя")
except:
    print("Что-то не так")

print(1 + 1)