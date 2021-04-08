try:
    print(1 / 0)
except ZeroDivisionError:
    print(2 / 0)
finally:
    print("Ничего не происходит")