"""Contains `Entity` class."""

from dataclasses import dataclass

from pygame import Vector2


@dataclass(eq=False)
class Entity:
    """Generic circular entity. Hashable."""

    position: Vector2
    velocity: Vector2 | None = None
    radius: int = 0

    def __post_init__(self) -> None:
        if self.velocity is None:
            self.velocity = Vector2(0, 0)
