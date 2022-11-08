import requests


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


class Test:
    def __hello(self):
        return print("hello")

    def _world(self):
        return print('world')

new = Test()

# new._Test__hello();new._world()

class Hello:
    def __init__(self):
        print("Hello")


class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("world!")


hello = Hello()
helloworld = Hello_World()


class Computer:
    def calculate(self):
        print(" 1+2=3 ")


class Display:
    def display(self):
        print("-214=-12-0=1203=-345-2395=0923=-05692-3wokjed;lkasjf.mnewrnew")


class Smartphone(Computer, Display):
    ...


xiaomi = Smartphone()
xiaomi.display()
xiaomi.calculate()

def first():
    ...

class Site:
    ...

TEST = Site

import inspect

print(inspect.isbuiltin(requests))