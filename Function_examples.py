from ctypes import HRESULT
from email.utils import specialsre


def lucaine():
    """
    simple function that just prints hello
    :return:
    """
    print("hello!")

def lucaine2(name):
    """
    Simple function that lucaines a person
    :param name: The name of the person
    :return:
    """
    print(f"hello, {name}")
lucaine2("John")
lucaine2("Pork")

def special_op(a=1, b=1):
    """
    Speical op is 10xa+b
    :param a: first number
    :param b: second numbervalue, 10a+b
    :return:
    """
    return 10*a + b
print(special_op(10, 2))
print(special_op(2, 10))
result = special_op(8, 9)
print(f"the special op for 8 and 9 is: {result}")
print(special_op(b=8, a=9))
print(special_op())
print(special_op(a=9))

def bond_greet(name):
    print(f"the name is: {name}")

def bondise_name(first_name="James", last_name="Bond"):
    return f"{last_name}, {first_name} {last_name}"
print(bondise_name("john", "Pork"))
bond_greet(bondise_name(first_name="John", last_name="Pork"))
bond_greet(bondise_name())