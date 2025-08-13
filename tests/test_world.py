"""Tests for `Entity` class."""

from pygame import Vector2

from two_d_library.entity import Entity
from two_d_library.world import World


def test_create() -> None:
    """Test that `World` can be created, and initial state."""
    # arrange
    # act
    w = World(size=Vector2(1, 1))
    # assert
    assert w
    assert len(w.entities) == 0


def test_random_position() -> None:
    """TO DO."""
    # arrange
    w = World(size_from_sequence=(1, 1))
    # act
    w.random_position()


def test_random_position__centered_origin() -> None:
    """TO DO."""
    # arrange
    w = World(size_from_sequence=(1, 1), centered_origin=True)
    # act
    w.random_position()


def test_add_entity() -> None:
    """Test that an `Entity` can be added to the `World`."""
    # arrange
    w = World(size=Vector2(100, 100))
    e = Entity(id_=1, position=Vector2(), velocity=Vector2())
    # act
    w.add_entity(e)
    # assert
    assert w.entities == {e}
