"""Contains `Entity` class."""

from dataclasses import dataclass

from pygame import Vector2


@dataclass(eq=False, kw_only=True)
class Entity:
    """Generic circular entity. Hashable."""

    id_: int
    position: Vector2
    velocity: Vector2

    acceleration: Vector2 | None = None
    radius: float = 0

    def __hash__(self) -> int:
        return self.id_

    def move(self, delta_time: float) -> None:
        """Move the entity."""
        if self.acceleration:
            self.velocity += self.acceleration * delta_time

        self.position += self.velocity * delta_time
