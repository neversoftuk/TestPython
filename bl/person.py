from ctypes import cast


class Person:
  def __init__(x, name, age):
    x.name = name
    x.age = age

  def myfunc(obj):
    print("Hello my name is " + obj.name + " and he is " + str(obj.age) + " years old.")

