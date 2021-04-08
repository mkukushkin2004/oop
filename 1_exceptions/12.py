a = int(input())
b = int(input())
if a > b:
    print("a больше b")
else:
    assert a < b, "Это проблема"  # второй аргумент
    print("a меньше b")
