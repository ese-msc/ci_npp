"""Tests for toy package."""

import numpy as np

import toy


def test_circle_area():
    circle = toy.Circle(2)
    assert np.isclose(circle.area(), 4*np.pi)


def test_rectangle_area():
    rectangle = toy.Rectangle(2, 3)
    assert rectangle.area() == 6


def test_rectangle_mean_side():
    rectangle = toy.Rectangle(2, 3)
    assert np.isclose(rectangle.mean_side(), 2.5)


def test_rectangle_perimeter():
    rectangle = toy.Rectangle(2, 3)
    assert np.isclose(rectangle.perimeter(), 10.0)


def test_ratio_perimeter_mean_side():
    assert np.isclose(toy.ratio_perimeter_mean_side(toy.Circle(1)), np.pi)
    assert np.isclose(toy.ratio_area_mean_side(toy.Circle(2)), np.pi)
