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

    size: Vector2 = field(init=False)
    entities: set[Entity] = field(default_factory=set)
    centered_origin: bool = field(default=False)

    def __post_init__(self, size_from_sequence: Sequence[int]) -> None:
        self.size = Vector2(size_from_sequence)

    def __str__(self) -> str:
        """Human-readable description."""
        return f"{type(self).__name__}(size={self.size})"

    def is_in_bounds(self, position: Vector2) -> bool:
        """Return whether `position` is within the world."""
        if self.centered_origin:
            magnitude = self.size / 2
            return abs(position.x) <= magnitude.x and abs(position.y) <= magnitude.y

        return 0 <= position.x <= self.size.x and 0 <= position.y <= self.size.y

    def random_position(self) -> Vector2:
        """Return a random position within the world."""
        if self.centered_origin:
            magnitude = self.size / 2
            return Vector2(
                random.uniform(-magnitude.x, magnitude.x),
                random.uniform(-magnitude.y, magnitude.y),
            )

        return Vector2(
            random.uniform(0, self.size.x),
            random.uniform(0, self.size.y),
        )

    def add_entity(self, entity: Entity) -> None:
        """Add `entity` to the world."""
        entity.id_ = len(self.entities)
        self.entities.add(entity)
