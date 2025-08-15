"""Contains `World` class."""

import random
from collections.abc import Sequence
from dataclasses import InitVar, dataclass, field

from pygame import Vector2

from two_d_library.entity import Entity


@dataclass(kw_only=True)
class World:
    """Rectangular."""

    size_from_sequence: InitVar[tuple[int, int]]

    centered_origin: bool = field(default=False)

    size: Vector2 = field(init=False)
    entities: set[Entity] = field(default_factory=set)

    _origin_offset: Vector2 = field(init=False)

    def __post_init__(self, size_from_sequence: Sequence[int]) -> None:
        self.size = Vector2(size_from_sequence)
        self._origin_offset = self.size / 2 if self.centered_origin else Vector2(0, 0)

    def __str__(self) -> str:
        """Human-readable description."""
        return f"{type(self).__name__}(size={self.size})"

    def position_is_in_bounds(self, *, position: Vector2, offset: float = 0) -> bool:
        """Return whether `position` is within the world.

        -ve/+ve offset: offset in/out from edge.
        """
        return (
            -offset <= position.x <= self.size.x + offset + self._origin_offset.x
            and -offset <= position.y <= self.size.y + offset + self._origin_offset.y
        )

    def random_position(self) -> Vector2:
        """Return a uniformly distributed random position within the world."""
        return Vector2(
            random.uniform(0, self.size.x + self._origin_offset.x),
            random.uniform(0, self.size.y + self._origin_offset.y),
        )

    def random_edge_position(self, offset: float = 0) -> Vector2:
        """Return a random position on or offset from the edge of the world.

        Uniformly distributed.

        -ve/+ve offset: offset in/out from edge.
        """
        sx, sy = self.size + Vector2(2 * offset)
        distance = random.uniform(0, 2 * sx + 2 * sy)
        if distance < sx:
            point = Vector2(distance, 0)
        elif distance < sx + sy:
            point = Vector2(sx, distance - sx)
        elif distance < 2 * sx + sy:
            point = Vector2(distance - sx - sy, sy)
        else:
            point = Vector2(0, distance - 2 * sx - sy)

        return point + self._origin_offset - Vector2(offset)

    def add_entity(self, entity: Entity) -> None:
        """Add `entity` to the world."""
        entity.id_ = len(self.entities)
        self.entities.add(entity)
