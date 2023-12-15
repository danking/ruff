x: "int" | str  # TCH006
x: ("int" | str) | "bool"  # TCH006


def func():
    x: "int" | str  # OK
