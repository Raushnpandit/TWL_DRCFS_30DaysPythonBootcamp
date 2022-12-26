class Animal:
    def __imit__(self, name: str, age: int, type_: str) -> Name:
        self.name = name
        self.age = age
        self.type_ = type_

        # private attribution
        self._ate = False


    def __str__(self):
        return f"I am {self.name}, my age is {self.age} and I'm a {self.type_}."

    def _do_something_private(Self) -> none:
        ...

    def eat_food(self):
        self._ate = True

    def eat_food(self):
        return self._ate
       

class Dog(Animal):
    def __init__(self, name: str, age: int) -> None:
        self.name


kalu = Animal('kalu', 5|
print|kalu) 