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
## Catching bugs

---

# Why add type hints?
## Auto-Completion

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

* How to choose the right type (Iterable vs List vs )
* Callables & Generators
* User-Defined Types
* Generics
* Overload & Cast
* TYPE_CHECKING
* Libraries that take advantage of type hints (FastAPI, Typer)
* Future of type hints