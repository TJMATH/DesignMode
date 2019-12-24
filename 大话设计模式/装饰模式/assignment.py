'''
author: kyang
task: 装饰模式实现小菜扮靓
'''

class Person(object):
    def __init__(self, name='Cai'):
        self.name = name

    def show(self):
        print(self.name)

class Decorator(Person):
    def __init__(self):
        super().__init__()
        self.person = None

    def get_person(self, person):
        self.person = person

class Tshirt(Decorator):
    def show(self):
        self.person.show()
        print('T-shirt')

class ABC(Decorator):
    def show(self):
        self.person.show()
        print('ABC')

class DEF(Decorator):
    def show(self):
        self.person.show()
        print('DEF')

class QWE(Decorator):
    def show(self):
        self.person.show()
        print('QWE')

def decorat(person, cls):
    new_person = cls()
    new_person.get_person(person)
    return new_person

def test():
    person = Person()
    person = decorat(person, Tshirt)
    person = decorat(person, ABC)
    person = decorat(person, DEF)
    person = decorat(person, QWE)
    person.show()

if __name__ == '__main__':
    test()