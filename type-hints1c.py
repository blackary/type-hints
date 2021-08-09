from typing import Dict, List, Tuple

mylist1 = []  # mypy error -- must add type annotation
mylist2: list = []
# doesn't give any more detail than the first,
# just that it's a list of *something*
mylist3: List = []  # equivalent to the first two
mylist4: List[str] = []  # tells it it's a list of strings

# No issues with mypy
mylist3.append(True)
mylist3.append(str)
mylist3.append(1.2)

# mypy error
mylist4.append(4)

for item in mylist4:
    item.upper()


# mypy error
mydict1 = {}  # mypy error -- should add type
mydict2: dict = {}  # same as above, but explicit
mydict3: Dict = {}  # same as above, but explicit
mydict4: Dict[str, float]  # keys are strs, values are floats


def get_point() -> Tuple[float, float]:
    return 1.0, 1.0
