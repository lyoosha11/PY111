import string

"""TASK-2"""


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, disc):
        res_price = self._price * (100 - disc) / disc
        return res_price


class Small_house(House):
    def_area = 40

    def __init__(self, price):
        super().__init__(Small_house.def_area, price)


class Human(Small_house):
    default_name = 'Alexey'
    default_age = 29

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name - {self.name}')
        print(f'Age - {self.age}')
        print(f'Money - {self.__money}')
        print(f'House - {self.__house}')

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def eam_money(self, salary):
        self.__money += salary
        return f'Cash - {self.__money}'

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, disc):
        price = house.final_price(disc)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Не хватает денег')


my_house = Small_house(100)
man = Human('Alexey', 29)
man.info()
man.buy_house(my_house, 10)
print('-' * 10)
man.eam_money(125)
man.info()
man.buy_house(my_house, 10)
print('-' * 10)
man.eam_money(250)
man.info()
print('-' * 10)
man.buy_house(my_house, 50)
man.info()


"""TASK-3"""


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        return self.lang

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def __letters_num(self):
        return EngAlphabet.__letters_num()

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return 'Yes'
        else:
            return 'No'

    @staticmethod
    def example():
        return 'Text in English'


word_en = EngAlphabet()
print(word_en.print())
print(word_en.letters_num())
print(word_en.is_en_letter('S'))
print(word_en.is_en_letter('Т'))
print(word_en.example())


"""TASK-DZ"""


class Tomato:
    states = {"rudimentary": 1, "stem": 2, "fetus": 3}

    def __init__(self, index):
        self._index = index
        self._state = self.states["rudimentary"]

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 3:
            return 'The tomato is ripe'
        return 'Not ripe yet'


class TomatoBush:

    def __init__(self, amount):
        self.tomatoes = [Tomato(index) for index in range(0, amount)]

    def grow_all(self):
        for tomat in self.tomatoes:
            tomat.grow()

    def all_are_ripe(self):
        return all([tomat.is_ripe() for tomat in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardner:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')
        # self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print('The tomato is ripe')
            self._plant.give_away_all()
        else:
            print('Not ripe yet')

    @staticmethod
    def knowledge_base():
        return "Reference Information"


print(Gardner.knowledge_base())
vegies = TomatoBush(5)
worker = Gardner('Alexey', vegies)

worker.harvest()
worker.work()


