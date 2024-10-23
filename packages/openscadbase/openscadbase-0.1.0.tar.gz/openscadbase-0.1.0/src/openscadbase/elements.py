from .base import Base2D, Base3D, Numeric

Point2D = tuple[Numeric, Numeric]


class CustomBase2D(Base2D):
    def __init__(self) -> None:
        self._element: Base2D

    def __repr__(self) -> str:
        return self._element.__repr__()


class Circle(Base2D):
    def __init__(self, r: Numeric, n: int | None = None, outer=False) -> None:
        self._r = r
        self._n = n
        self._outer = outer

    def __repr__(self) -> str:
        return f'circle({f"$fn={self._n, }" if self._n else ""}r={self._r}{"/cos(180/fn)" if self._outer else ""})'


class Elipsis(CustomBase2D):
    def __init__(
        self, rx: Numeric, ry: Numeric, n: int | None = None, outer=False
    ) -> None:
        self._element = Circle(1, n, outer).scale(rx, ry)


class Poligon(Base2D):
    def __init__(self, outline: list[Point2D], *holes: list[Point2D]) -> None:
        lists = [outline] + list(holes)
        self._points = [e for l in lists for e in l]
        self._paths = self.enumerate(lists, 0)

    def __repr__(self) -> str:
        return f"polygon(points={[list(p) for p in self._points]}, paths={self._paths}, convexity=10);"

    def enumerate(self, paths: list[list[Point2D]], last: int) -> list[list[int]]:
        print(paths, last)
        segment_path = paths.pop(0)

        segment_enumerations = list(range(last, last + len(segment_path)))
        last += len(segment_enumerations)

        if len(paths) == 0:
            return [segment_enumerations]

        enumerations = [segment_enumerations] + self.enumerate(paths, last)
        return enumerations


class Openscad2D(Base2D):
    def __init__(self, openscad: str) -> None:
        self._element = openscad
        super().__init__()

    def __repr__(self) -> str:
        return self._element


Point3D = tuple[Numeric, Numeric, Numeric]


class CustomBase3D(Base3D):
    def __init__(self) -> None:
        self._element: Base3D

    def __repr__(self) -> str:
        return self._element.__repr__()


class Cube(Base3D):
    def __init__(self, dx: Numeric, dy: Numeric, dz: Numeric, center=False) -> None:
        self._dx = dx
        self._dy = dy
        self._dz = dz
        self._center = str(center).lower()

    def __repr__(self) -> str:
        return f"cube([{self._dx}, {self._dy}, {self._dz}], center={self._center});"


class Sphere(Base3D):
    def __init__(self, r: Numeric, n: int | None = None) -> None:
        self._r = r
        self._n = n

    def __repr__(self) -> str:
        return f'sphere({f"$fn={self._n}, " if self._n else ""}r={self._r})'


class Cylinder(Base3D):
    def __init__(
        self,
        h: Numeric,
        r: Numeric,
        n: int | None = None,
        center=False,
        outer=False,
    ) -> None:
        self._h = h
        self._r = r
        self._n = n
        self._center = str(center).lower()
        self._outer = outer

    def __repr__(self) -> str:
        return f'cylinder({f"$fn={self._n}, " if self._n else ""}h={self._h}, r={self._r}{"/cos(180/fn)" if self._outer else ""}, center={self._center}'


class Cone(Base3D):
    def __init__(
        self,
        h: Numeric,
        rb: Numeric,
        rt: Numeric,
        n: int | None = None,
        center=False,
        outer=False,
    ) -> None:
        self._h = h
        self._rb = rb
        self._rt = rt
        self._n = n
        self._center = str(center).lower()
        self._outer = outer

    def __repr__(self) -> str:
        return f'cylinder({ f"$fn={self._n}, " if self._n else ""}h={self._h}, r1={self._rb}{"/cos(180/fn)" if self._outer else ""}, r2={self._rt}{"/cos(180/fn)" if self._outer else ""}, center={self._center}'


class Openscad3D(Base3D):
    def __init__(self, openscad: str) -> None:
        self._element = openscad
        super().__init__()

    def __repr__(self) -> str:
        return self._element
