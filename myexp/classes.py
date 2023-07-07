# class Person:
#     pass

# print(type(Person))

# print(type)

# print(Person.__name__)

# p = Person()

# print(p)
# print(type(p))
# print(type(p) is p.__class__)

# print(isinstance(p, Person))

# class Program:
#     language = 'Python'
#     version = '3.6'
#     @classmethod
#     def say_hello_cls(cls):
#         print(f'program attributes are {Program.language}  {Program.version}')
#         print(f'program attributes are {cls.language}  {cls.version}')
#     def say_hello(self):
#         print(f'program attributes are {Program.language}  {Program.version}')
#         # print(f'program attributes are {cls.language}  {cls.version}')

# print(type(Program.say_hello_cls))
# # this is function 
# print(type(Program.say_hello))

# p = Program()
# print(p.__dict__)
# # the same function turned method bound to an object
# print(type(p.say_hello))
# # monkey patch classes 
# Program.runTimefunc = lambda *args: f'The args are {args} and number of args is {len(args)}'
# print(type(p.runTimefunc))
# print(p.runTimefunc(12, 100))
# print(hex(id(p)))
# # monkey patching functions in instance coz its not defined in class. Functions defined in class become method bounded to object
# p.do_some = lambda *args: f'This is a function not a method {args} amd number of args {len(args)}'
# print(type(p.do_some))
# print(p.do_some(12,100))
# Create inheritance without inheritance ..monkey patching 
from types import MethodType
from typing import Any
class Worker:
    def __init__(self,name:str) -> None:
        self.name = name
    def register_work(self, func) -> None:
        # self._work_func = MethodType(func, self)
        setattr(self, '_work_func', MethodType(func, self))
    def do_work(self, *args) -> Any:
        work_func = getattr(self, '_work_func',None)
        if work_func:
            return work_func(*args)
        else:
            raise AttributeError('First register work')
        
designer = Worker('Haldi')
player = Worker('HP')
driver = Worker('SC')

designer.register_work(lambda *args: print(f' Designing with {args[1:]}'))
player.register_work(lambda *args: print(f' Playing with {args[1:]}'))
driver.register_work(lambda *args: print(f' Driving with {args[1:]}'))
try:
    designer.do_work(12, 100, "design_it")
    player.do_work(66, 200, "play_it")
    driver.do_work(400, 600, "drive_it")
    print(driver.__dict__)
except Exception as e:
    print(e)

# print(Program.__name__)

# print(Program.language)

# print(Program.version)

# Program.version = '3.7'

# print(Program.version)

# print(getattr(Program, 'version'))

# setattr(Program, 'version', '1119996')

# print(getattr(Program, 'version'))

# print(Program.__dict__)
# Program.say_hello()
# getattr(Program, 'say_hello')()
# Program.__dict__['say_hello'](Program)