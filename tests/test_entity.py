"""Tests for `Entity` class."""

from pygame import Vector2

from two_d_library.entity import Entity


def test_create() -> None:
    """Test `Entity` can be created, and initial state."""
    # arrange
    # act
    e = Entity(id_=1, position=Vector2(), velocity=Vector2())
    # assert
    assert e.radius == 0
    assert e.position == Vector2(0, 0)
    assert e.velocity == Vector2(0, 0)
