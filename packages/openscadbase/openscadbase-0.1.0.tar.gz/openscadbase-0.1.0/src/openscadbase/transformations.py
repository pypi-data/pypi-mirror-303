from __future__ import annotations

from .base import Base, Base2D, Base3D, Numeric


class ScaleTransformation:
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"scale({self._transformation}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class ScaleTransformation2D(ScaleTransformation, Base2D):
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base2D) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)


class ScaleTransformation3D(ScaleTransformation, Base3D):
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base3D) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)


class ResizeTransformation:
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"resize({self._transformation}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class ResizeTransformation2D(ResizeTransformation, Base2D):
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base2D) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)


class ResizeTransformation3D(ResizeTransformation, Base3D):
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base3D) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)


class RotateTransformation:
    def __init__(self, ax: Numeric, ay: Numeric, az: Numeric, *elements: Base) -> None:
        self._transformation = [ax, ay, az]
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"rotate({self._transformation}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class RotateTransformation2D(RotateTransformation, Base2D):
    def __init__(
        self, ax: Numeric, ay: Numeric, az: Numeric, *elements: Base2D
    ) -> None:
        self._transformation = [ax, ay, az]
        self._elements = list(elements)


class RotateTransformation3D(RotateTransformation, Base3D):
    def __init__(
        self, ax: Numeric, ay: Numeric, az: Numeric, *elements: Base3D
    ) -> None:
        self._transformation = [ax, ay, az]
        self._elements = list(elements)


class TranslateTransformation:
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"translate({self._transformation}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class TranslateTransformation2D(TranslateTransformation, Base2D):
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base2D) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)


class TranslateTransformation3D(TranslateTransformation, Base3D):
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base3D) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)


class MirrorTransformation:
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"mirror({self._transformation}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class MirrorTransformation2D(MirrorTransformation, Base2D):
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base2D) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)


class MirrorTransformation3D(MirrorTransformation, Base3D):
    def __init__(self, x: Numeric, y: Numeric, z: Numeric, *elements: Base3D) -> None:
        self._transformation = [x, y, z]
        self._elements = list(elements)


class AffineTransformation:
    def __init__(self, matrix: list, *elements: Base) -> None:
        self._transformation = matrix
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"multmatrix({self._transformation}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class AffineTransformation2D(AffineTransformation, Base2D):
    def __init__(self, matrix: list, *elements: Base2D) -> None:
        self._transformation = matrix
        self._elements = list(elements)


class AffineTransformation3D(AffineTransformation, Base3D):
    def __init__(self, matrix: list, *elements: Base3D) -> None:
        self._transformation = matrix
        self._elements = list(elements)


class OffsetRadialTransformation2D(Base2D):
    def __init__(self, r: Numeric, *elements: Base2D) -> None:
        self._transformation = r
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"offset(r={self._transformation}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class OffsetDeltaTransformation2D(Base2D):
    def __init__(self, d: Numeric, chamfer: bool, *elements: Base2D) -> None:
        self._transformation = (d, chamfer)
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"offset(d={self._transformation[0]}, chamfer={str(self._transformation[0]).lower()}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class MinkowskiSumTransformation:
    def __init__(self, *elements: Base) -> None:
        self._elements = list(elements)

    def __repr__(self) -> str:
        return "minkowski(){ " + " ".join([e.__repr__() for e in self._elements]) + " }"


class MinkowskiSumTransformation2D(MinkowskiSumTransformation, Base2D):
    def __init__(self, *elements: Base2D) -> None:
        self._elements = list(elements)


class MinkowskiSumTransformation3D(MinkowskiSumTransformation, Base3D):
    def __init__(self, *elements: Base3D) -> None:
        self._elements = list(elements)


class ConvexHullTransformation:
    def __init__(self, *elements: Base) -> None:
        self._elements = list(elements)

    def __repr__(self) -> str:
        return "hull(){ " + " ".join([e.__repr__() for e in self._elements]) + " }"


class ConvexHullTransformation2D(ConvexHullTransformation, Base2D):
    def __init__(self, *elements: Base2D) -> None:
        self._elements = list(elements)


class ConvexHullTransformation3D(ConvexHullTransformation, Base3D):
    def __init__(self, *elements: Base3D) -> None:
        self._elements = list(elements)


class LinearExtrudeTransformation3D(Base3D):
    def __init__(
        self,
        height: Numeric,
        center: bool = True,
        convexity: int | None = None,
        twist: Numeric | None = None,
        slice: Numeric | None = None,
        scale: Numeric | tuple[Numeric, Numeric] | None = None,
        *elements: Base2D,
    ) -> None:
        self._height = height
        self._center = str(center).lower()
        self._convexity = convexity
        self._twist = twist
        self._slices = slice
        self._scale = scale
        self._elements = list(elements)

    def __repr__(self) -> str:
        command = f"linear_extrude(height={self._height}, center={self._center}"
        if self._convexity is not None:
            command += f", convexity={self._convexity}"
        if self._twist is not None:
            command += f", twist={self._twist}"
        if self._slices is not None:
            command += f", slices={self._slices}"
        if self._scale is not None:
            if isinstance(self.scale, tuple):
                command += f", scale={list(self.scale)}"
            else:
                command += f", scale={self.scale}"

        return (
            command
            + ", $fn = 16){ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class RotateExtrudeTransformation3D(Base3D):
    def __init__(
        self, angle: Numeric = 360, convexity: int = 10, *elements: Base2D
    ) -> None:
        self._angle = angle
        self._convexity = convexity
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"rotate_extrude(angle={self._angle}, convexity={self._convexity}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )


class ProjectionTransformation2D(Base2D):
    def __init__(self, cut=False, *elements: Base3D) -> None:
        self._cut = str(cut).lower()
        self._elements = list(elements)

    def __repr__(self) -> str:
        return (
            f"projection(cut={self._cut}){{ "
            + " ".join([e.__repr__() for e in self._elements])
            + " }"
        )
