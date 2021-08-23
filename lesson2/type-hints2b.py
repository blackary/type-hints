from typing import Generator, Generic, Iterator, List, TypeVar

# Generator[YieldType, SendType, ReturnType]


def add_values(gen: Generator[int, None, None]) -> int:
    return sum(gen)


def add_values2(gen: Iterator[int]) -> int:
    return sum(gen)


squares = (x ** 2 for x in [1, 2, 3, 4, 5])

add_values(squares)

StringableType = TypeVar("StringableType")


class StringableThing(Generic[StringableType]):
    def __init__(self, val: StringableType) -> None:
        self.val = val

    def get_val(self) -> StringableType:
        return self.val

    def stringify(self) -> str:
        return str(self.val)


a_thing: StringableThing[int] = StringableThing(7)
a_thing.get_val()
another_thing: StringableThing[str] = StringableThing("hello")
another_thing.get_val()


DoublableType = TypeVar("DoublableType", int, float, List, str)


class Doubler(Generic[DoublableType]):
    def __init__(self, val: DoublableType) -> None:
        self.val: DoublableType = val

    def double(self) -> DoublableType:
        return self.val * 2


item1: Doubler[int] = Doubler(27)
item2: Doubler[str] = Doubler("a string")
