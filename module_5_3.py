# 1. __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# 2. Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
# результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# 3. __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# 4. __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}.'

    def __eq__(self, other):
        return self.name != other.name and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + isinstance(value, int)

    def __radd__(self, value):
        return self.number_of_floors + isinstance(value, int)

    def __iadd__(self, value):
        return self.number_of_floors + isinstance(value, int)



h1 = House('ЖК Гулливер', 25)
h2 = House('Hytte', 12)

print(h1)                                                          # Название и этажи
print(h2)                                                          # Название и этажи
print()
print(f'Равное кол-во этажей: {h1 == h2}')                         # __eq__
print()
h2.number_of_floors = h2.number_of_floors + 13                     # __add__
print(h2)                                                          # Название и этажи
print(f'Равное кол-во этажей: {h1 == h2}')                         # __eq__
print()
h1.number_of_floors += 10                                          # __iadd__
print(h1)                                                          # Название и этажи
print()
h2.number_of_floors = 10 + h2.number_of_floors                     # __radd__
print(h2)                                                          # Название и этажи
print()
print(h1 > h2)                               # __gt__
print(h1 >= h2)                              # __ge__
print(h1 < h2)                               # __lt__
print(h1 <= h2)                              # __le__
print(h1 != h2)                              # __ne__
