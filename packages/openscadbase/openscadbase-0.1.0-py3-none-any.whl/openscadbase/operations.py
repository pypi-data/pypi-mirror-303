from .base import Base, Base2D, Base3D


class UnionOperation:
    def __init__(self, *elements: Base) -> None:
        self._elements = list(elements)

    def __repr__(self) -> str:
        return "union() {" + " ".join([e.__repr__() for e in self._elements]) + "}"


class UnionOperation2D(UnionOperation, Base2D):
    def __init__(self, *elements: Base2D) -> None:
        self._elements = list(elements)


class UnionOperation3D(UnionOperation, Base3D):
    def __init__(self, *elements: Base3D) -> None:
        self._elements = list(elements)


class DifferenceOperation:
    def __init__(self, *elements: Base) -> None:
        self._elements = list(elements)

    def __repr__(self) -> str:
        return "difference() {" + " ".join([e.__repr__() for e in self._elements]) + "}"


class DifferenceOperation2D(DifferenceOperation, Base2D):
    def __init__(self, *elements: Base2D) -> None:
        self._elements = list(elements)


class DifferenceOperation3D(DifferenceOperation, Base3D):
    def __init__(self, *elements: Base3D) -> None:
        self._elements = list(elements)


class IntersectionOperation:
    def __init__(self, *elements: Base) -> None:
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            "intersection() {" + " ".join([e.__repr__() for e in self._elements]) + "}"
        )


class IntersectionOperation2D(IntersectionOperation, Base2D):
    def __init__(self, *elements: Base2D) -> None:
        self._elements = list(elements)


class IntersectionOperation3D(IntersectionOperation, Base3D):
    def __init__(self, *elements: Base3D) -> None:
        self._elements = list(elements)
