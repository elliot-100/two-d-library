"""Contains `Universe` class."""

import random
from dataclasses import dataclass, field

from pygame import Vector2

from two_d_library.entity import Entity


@dataclass(kw_only=True)
class Universe:
    """Rectangular."""

    size: Vector2
    entities: set[Entity] = field(default_factory=set)
    centered_origin: bool = field(default=False, kw_only=True)

    def is_in_bounds(self, position: Vector2) -> bool:
        """Return whether `position` is within the universe."""
        if self.centered_origin:
            magnitude = self.size / 2
            return abs(position.x) < magnitude.x and abs(position.y) < magnitude.y

        return 0 <= position.x < self.size.x and 0 <= position.y < self.size.y

    def random_position(self) -> Vector2:
        """Return a random position within the universe."""
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
        """Add `entity` to the universe."""
        entity.id_ = len(self.entities)
        self.entities.add(entity)
