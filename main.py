class Grandparent:
    height = 170
    satiety = 100
    age = 60


class Parent(Grandparent):
    age = 40


class Child(Parent):
    height = 170
    age = 14

    def __init__(self):
        print(self.height, self.satiety, self.age)


class Monster:
    ...


me = Child()
monster = Monster()

for obj in (me, monster):
    if isinstance(obj, Grandparent):
        print("You are a human")
    else:
        print("You are a monster")
