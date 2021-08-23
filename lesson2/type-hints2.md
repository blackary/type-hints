---
marp: true
theme: gaia
---
<!-- class: lead -->

# Python Type Hints, Part 2
#### Python Office Hours 2021-08-23

---
<!-- class: -->

# Topics to Cover

* Brief Review
* Callables & Generators
* User-Defined Type Aliases
* Generics
* Overload & Cast
* TYPE_CHECKING
* Mypy settings
* Libraries that take advantage of type hints (FastAPI, Typer, etc.)
* Future of type hints

---
<!-- class: invert -->

# Brief Review

Type hints are:

* Optional, structured comments about the types of variables, arguments, return types, etc. for modern python (>=3.0)
* Can be parsed and checked by automated tools (e.g. `mypy`) to check for consistency
* Can be added piecemeal
* Can help catch bugs, and reveal underlying assumptions
* Add readability
* Allow for smarter auto-complete

---

# Callables & Generators

`Callable[[list_of_argument_types], return_type]`

```python
from typing import Callable

# Note: the Callable's None is required
def apply_transform(df: pd.DataFrame, transform: Callable[[pd.DataFrame], None]):
    transform(df)

def fetch_data(fetcher: Callable[..., pd.DataFrame], **kwargs) -> pd.DataFrame:
    return fetcher(**kwargs)

def create_grid(arg1: int, arg2: int, grid_fn: Callable[[int, int], np.ndarray]) -> np.ndarray:
    return grid_fn(arg1, arg2)
```

---

# Callables & Generators

Informing the editor:

![](../figs/callable.png)

Adding this annotation allows the editor to intelligently describe what can be passed into this function.

---
# Callables & Generators

`Generator[YieldType, SendType, ReturnType]`

Much of the time, your generators probably have only a YieldType

```python
def add_values(gen: Generator[int, None, None]) -> int:
    return sum(gen)
```

In this case, `Iterator` is probably the best choice (more on this later)
```python
def add_values2(gen: Iterator[int]) -> int:
    return sum(gen)
```

---

# User-Defined Type Aliases

If you find yourself using a particular complicated type regularly (e.g. `Dict[Union[str, int], Callable...]`), or a type has a particular meaning in this code context (e.g. this type of dictionary always represents model options), it can be helpful to define a custom name for that class.

```python
ModelOptionsType = Dict[Union[str, int], Union[int, np.ndarray]]

def create_model(options: ModelOptionsType) -> ...
```

---
# User-Defined Type Aliases

An Example from `pandas._typing`

```python
PythonScalar = Union[str, int, float, bool]
DatetimeLikeScalar = Union["Period", "Timestamp", "Timedelta"]
PandasScalar = Union["Period", "Timestamp", "Timedelta", "Interval"]
Scalar = Union[PythonScalar, PandasScalar]
```

---
# Generics

Types like `List`, `Dict`, etc. are Generic container types, which can be containers made up of any different type of object.

You can define your own generic types, which can be used as types, and with `[]` syntax. More importantly, they can be used to create custom classes which use the `[]` sytax.


---
# Generics

```python
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
```
---
# Generics

Generic types can be constrained

```python
DoublableType = TypeVar("DoublableType", int, float, List, str)

class Doubler(Generic[DoublableType]):
    def __init__(self, val: DoublableType) -> None:
        self.val: DoublableType = val

    def double(self) -> DoublableType:
        return self.val * 2

item1: Doubler[int] = Doubler(27)
item2: Doubler[str] = Doubler("a string")
```
---
# Overload & Cast

---
# TYPE_CHECKING

---
# Mypy Settings

---
# Libaries that use Type Hints

---
# Future of type hints
---

# What did we cover?
<!-- class: -->

* Brief Review
* Callables & Generators
* User-Defined Type Aliases
* Generics
* Overload & Cast
* TYPE_CHECKING
* Mypy settings
* Libraries that take advantage of type hints (FastAPI, Typer, etc.)
* Future of type hints
---

# Future Topics

* Callables & Generators
* User-Defined Types
* Generics
* Overload & Cast
* TYPE_CHECKING
* Mypy settings
* Libraries that take advantage of type hints (FastAPI, Typer, etc.)
* Future of type hints