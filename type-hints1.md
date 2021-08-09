---
marp: true
theme: gaia
---
<!-- class: lead -->

# Python Type Hints
#### Python Office Hours 2021-08-09

---
<!-- class: -->

# Topics to Cover

* What is type hinting?
* What would you want to add type hints to your code?
* Basic type hinting (str, int, etc.)
* Using type checkers
* Types with parameters: Lists, Tuples & Dictionaries
* More complex types (Union, Optional, Any)
* Where to start
* Where to learn more

---
<!-- class: invert -->

# What is type hinting

```python
def graduate(name: str) -> str:
    return "Dr. " + name

entries: List[str] = []
```

* Type hints ~ comments about variable types, function inputs, return types, etc.
* Standardized formats (as opposed to docstring comments) mean that automated type checkers can check them for consistency.
* Not required, and can be added gradually

---
# Why add type hints?
## What is this, C?

```c
int id;
double price;
```
Seems like worrying about types takes away some of the beauty and simplicity of Python.
Seems un-pythonic -- isn't python supposed to use duck-typing?

---
# Why add type hints?
## Catching bugs preemptively

```python
def uppercase(val):
    """Takes a string and upper-cases it"""
    return val.upper()

uppercase("hello")
uppercase(6)
```
Perfectly sytactically valid
Results in a runtime error, but it would be nice to catch it beforehand

---
# Why add type hints?
## Catching bugs preemptively

![](figs/argument-error.png)

---

# Why add type hints?
## Auto-Completion
Labeling types also are available to inform your editor about the objects in question

Your editor can figure out what methods are available on an object


Example: working with Path objects

---
# Why add type hints?
## Better code documentation
Makes the intended use of a function or class explicit
Allows you to make your duck-typing more explicit -- what exactly am I assuming will be the characteristics of the things that are passed in & returned from this function?
* Did you just need an input that can be stringified?
* Did you need an input that has a particular method?
* Did you need something that can be iterated over?

---

# What did we cover?
<!-- class: -->

* What is type hinting?
* What would you want to add type hints to your code?
* Basic type hinting (str, int, etc.)
* Using type checkers
* Types with parameters Lists, Tuples & Dictionaries
* More complex types (Union, Optional, Any)
* Where to start?
* Where to learn more

---

# Future Topics

* How to choose the right type (e.g. Iterable vs List vs Sequence)
* Callables & Generators
* User-Defined Types
* Generics
* Overload & Cast
* TYPE_CHECKING
* Libraries that take advantage of type hints (FastAPI, Typer)
* Future of type hints