from __future__ import annotations

from typing import Union

Numeric = Union[int, float]


class Base:
    def __repr__(self) -> str:
        return NotImplemented


class Base2D(Base):
    def union(self, other: Base2D) -> Base2D:
        from .operations import UnionOperation2D

        return UnionOperation2D(self, other)

    def difference(self, other: Base2D) -> Base2D:
        from .operations import DifferenceOperation2D

        return DifferenceOperation2D(self, other)

    def intersection(self, other: Base2D) -> Base2D:
        from .operations import IntersectionOperation2D

        return IntersectionOperation2D(self, other)

    def scale(self, x: Numeric = 1, y: Numeric = 1, z: Numeric = 1) -> Base2D:
        from .transformations import ScaleTransformation2D

        return ScaleTransformation2D(x, y, z, self)

    def resize(self, x: Numeric = 0, y: Numeric = 0, z: Numeric = 0) -> Base2D:
        from .transformations import ResizeTransformation2D

        return ResizeTransformation2D(x, y, z, self)

    def rotate(self, ax: Numeric = 0, ay: Numeric = 0, az: Numeric = 0) -> Base2D:
        from .transformations import RotateTransformation2D

        return RotateTransformation2D(ax, ay, az, self)

    def translate(self, x: Numeric = 0, y: Numeric = 0, z: Numeric = 0) -> Base2D:
        from .transformations import TranslateTransformation2D

        return TranslateTransformation2D(x, y, z, self)

    def mirror(self, x: Numeric = 0, y: Numeric = 0, z: Numeric = 0) -> Base2D:
        from .transformations import MirrorTransformation2D

        return MirrorTransformation2D(x, y, z, self)

    def affine(self, matrix: list) -> Base2D:
        from .transformations import AffineTransformation2D

        return AffineTransformation2D(matrix, self)

    def minkowski_sum(self) -> Base2D:
        from .transformations import MinkowskiSumTransformation2D

        return MinkowskiSumTransformation2D(self)

    def convex_hull(self) -> Base2D:
        from .transformations import ConvexHullTransformation2D

        return ConvexHullTransformation2D(self)

    def offset_radial(self, r: Numeric) -> Base2D:
        from .transformations import OffsetRadialTransformation2D

        return OffsetRadialTransformation2D(r, self)

    def offset_delta(self, d: Numeric, chamfer=False) -> Base2D:
        from .transformations import OffsetDeltaTransformation2D

        return OffsetDeltaTransformation2D(d, chamfer, self)

    def linear_extrude(
        self,
        height,
        center: bool = True,
        convexity: int | None = None,
        twist: Numeric | None = None,
        slices: Numeric | None = None,
        scale: Numeric | tuple[Numeric, Numeric] | None = None,
    ) -> Base3D:
        from .transformations import LinearExtrudeTransformation3D

        return LinearExtrudeTransformation3D(
            height, center, convexity, twist, slices, scale, self
        )

    def rotate_extrude(self, angle: Numeric = 360, convexity: int = 10) -> Base3D:
        from .transformations import RotateExtrudeTransformation3D

        return RotateExtrudeTransformation3D(angle, convexity, self)


class Base3D(Base):
    def union(self, other: Base3D) -> Base3D:
        from .operations import UnionOperation3D

        return UnionOperation3D(self, other)

    def difference(self, other: Base3D) -> Base3D:
        from .operations import DifferenceOperation3D

        return DifferenceOperation3D(self, other)

    def intersection(self, other: Base3D) -> Base3D:
        from .operations import IntersectionOperation3D

        return IntersectionOperation3D(self, other)

    def scale(self, x: Numeric = 1, y: Numeric = 1, z: Numeric = 1) -> Base3D:
        from .transformations import ScaleTransformation3D

        return ScaleTransformation3D(x, y, z, self)

    def resize(self, x: Numeric = 0, y: Numeric = 0, z: Numeric = 0) -> Base3D:
        from .transformations import ResizeTransformation3D

        return ResizeTransformation3D(x, y, z, self)

    def rotate(self, ax: Numeric = 0, ay: Numeric = 0, az: Numeric = 0) -> Base3D:
        from .transformations import RotateTransformation3D

        return RotateTransformation3D(ax, ay, az, self)

    def translate(self, x: Numeric = 0, y: Numeric = 0, z: Numeric = 0) -> Base3D:
        from .transformations import TranslateTransformation3D

        return TranslateTransformation3D(x, y, z, self)

    def mirror(self, x: Numeric = 0, y: Numeric = 0, z: Numeric = 0) -> Base3D:
        from .transformations import MirrorTransformation3D

        return MirrorTransformation3D(x, y, z, self)

    def affine(self, matrix: list) -> Base3D:
        from .transformations import AffineTransformation3D

        return AffineTransformation3D(matrix, self)

    def minkowski_sum(self) -> Base3D:
        from .transformations import MinkowskiSumTransformation3D

        return MinkowskiSumTransformation3D(self)

    def convex_hull(self) -> Base3D:
        from .transformations import ConvexHullTransformation3D

        return ConvexHullTransformation3D(self)

    def project(self, cut=False) -> Base2D:
        from .transformations import ProjectionTransformation2D

        return ProjectionTransformation2D(cut, self)
