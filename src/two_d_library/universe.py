"""Contains `Universe` class."""

from dataclasses import dataclass, field

from pygame import Vector2

from two_d_library.entity import Entity


@dataclass
class Universe:
    """Rectangular with centred origin."""

    size: Vector2
    entities: set[Entity] = field(default_factory=set)

    def in_bounds(self, position: Vector2) -> bool:
        """Return whether `position` is within the universe."""
        magnitude = self.size / 2
        return abs(position.x) < magnitude.x and abs(position.y) < magnitude.y

    def add_entity(self, entity: Entity) -> None:
        """Add `entity` to the universe."""
        self.entities.add(entity)
