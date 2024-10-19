class Matrix:
    def __init__(self, array: list[list[int | float]]) -> None:
        self.array: list[list[int | float]] = array

        self.lines: int = len(array)
        self.columns: int = len(array[0])

        self.main_diagonal: list[int | float] = [array[i][i] for i in range(self.lines)]

    @property
    def reflexivity(self) -> str | None:
        if sum(self.main_diagonal) == self.columns:
            return "reflexive"

        if sum(self.main_diagonal) == 0:
            return "irreflexive"

        return None

    @property
    def symmetry(self) -> str:
        is_symmetrical: bool = True

        for line in range(self.lines):
            for column in range(self.columns):
                if line == column: continue

                if self.array[line][column] != self.array[column][line]:
                    is_symmetrical = False
                    break

        if is_symmetrical:
            return "symmetrical"

        is_antisymmetric: bool = True

        for line in range(self.lines):
            for column in range(self.columns):
                if line == column: continue

                if self.array[line][column] == self.array[column][line]:
                    is_antisymmetric = False
                    break

        if is_antisymmetric:
            return "antisymmetric"

        return "asymmetrical"

    @property
    def transitivity(self) -> str | None:
        for x in range(self.lines):
            for y in range(self.columns):
                if x == y: continue

                for z in range(self.lines):
                    if z == x or z == x: continue

                    if self.array[x][y] and self.array[y][z] and not self.array[x][y]: return None

        return "transitive"

    @property
    def connectivity(self) -> str | None:
        for x in range(self.lines):
            for y in range(self.columns):
                if self.array[x][y] == self.array[y][x]: continue

                if not (self.array[x][y] or self.array[y][x]):
                    return None

        return "coherent"
