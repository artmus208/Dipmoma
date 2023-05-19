def make_lie(method):
    def wrapper(self):
        lie = -3
        self.age += lie
        return method(self)
    
    return wrapper


class Artur:
    def __init__(self, age) -> None:
        self.age = age
        self.name = "Arthur"

    @make_lie
    def say_hello(self):
        print(
            f"Привет, меня зовут {self.name}, мне {self.age}"
        )

a = Artur(age=22)
a.say_hello()