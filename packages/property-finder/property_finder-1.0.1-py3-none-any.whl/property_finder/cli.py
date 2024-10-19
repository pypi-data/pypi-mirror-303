from pathlib import Path

import typer

from .matrix import Matrix

app = typer.Typer()


class ParamError(Exception):
    pass


def get_matrix_from_file(file: Path, lines: int, columns: int) -> Matrix:
    array: list[list[int | float]] = [[0 for _ in range(columns)] for _ in range(lines)]

    with open(file, "r") as file:
        for line in range(lines):
            string = file.readline().replace("\n", "").strip().split(" ")

            if len(string) != columns:
                print(len(string), columns)
                raise ParamError("Wrong value of column")

            for column, element in enumerate(string):
                value = int(float(element)) if int(float(element)) == float(element) else float(element)
                array[line][column] = value

    return Matrix(array)


def get_output(matrix: Matrix) -> str:
    return (
        f"This relation is:"
        f"{"\n\t- " + matrix.reflexivity if matrix.reflexivity is not None else ""}"
        f"{"\n\t- " + matrix.symmetry}"
        f"{"\n\t- " + matrix.transitivity if matrix.transitivity is not None else ""}"
        f"{"\n\t- " + matrix.connectivity if matrix.connectivity is not None else ""}"
    )


@app.command()
def main(file: Path = Path("matrix.txt"), lines: int = 6, columns: int = 6):
    if not file.exists():
        print("No such file or directory")

    try:
        matrix = get_matrix_from_file(file, lines, columns)
        output = get_output(matrix)
        print(output)
    except ParamError:
        print("Check file path and/or line and column params")
