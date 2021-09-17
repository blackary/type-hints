import typer


def main(name: str, english: bool = True):
    if english is True:
        print(f"Hello {name}")
    else:
        print(f"Hola {name}")


if __name__ == "__main__":
    typer.run(main)
