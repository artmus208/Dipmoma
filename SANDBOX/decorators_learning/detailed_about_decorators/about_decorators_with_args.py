def my_own_decorator(func):
    def wrapper(arg1:int, arg2:int):
        print(f"Изменяю параметры...\nСтарые параметры:{arg1}, {arg2}")
        new_arg1 = arg1 + 2
        new_arg2 = arg2 + 2
        func(new_arg1, new_arg2)
        print(f"Изменил параметры...\nНовые параметры:{new_arg1}, {new_arg2}")

    return wrapper

@my_own_decorator
def add(a, b):
    print(a+b)


add(3, 5)
