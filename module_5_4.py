class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        house = super().__new__(cls) # создаем родительский класс который связывает new с init
        house.__init__(*args, **kwargs) # связываемся с init через house присваеваем аргументы new к init
        cls.houses_history.append(house.name) # говорим что нужно добавить в список имя
        # cls.houses_history.append(house.floor) # говорим что нужно добавить в список этаж
        return house

    def __init__(self, name, floor):
        self.name = name
        self.floor = floor
        return

    def __del__(self):
        House.houses_history.remove(self.name)
        print(f"{self.name} снесен но остается в памяти")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)