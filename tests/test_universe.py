"""Tests for `Entity` class."""

from pygame import Vector2

from two_d_library.entity import Entity
from two_d_library.universe import Universe


def test_create() -> None:
    """Test that `Universe` can be created, and initial state."""
    # arrange
    # act
    u = Universe(size=Vector2(1, 1))
    # assert
    assert u
    assert len(u.entities) == 0


def test_add_entity() -> None:
    """Test that an `Entity` can be added to the `Universe`."""
    # arrange
    u = Universe(size=Vector2(100, 100))
    e = Entity(id_=1, position=Vector2(), velocity=Vector2())
    # act
    u.add_entity(e)
    # assert
    assert u.entities == {e}
    assert e.id_ == 0
