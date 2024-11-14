import pytest
import math
from ..figures.circle import area, perimeter


class TestCircle:
    # given
    @pytest.mark.parametrize(
        "radius, expected",
        [
            (0, 0),
            (1, 3.141592653589793),
            (5, 78.53981633974483),
        ],
    )
    def test_area_valid_input(self, radius, expected):
        # when
        actual = area(radius)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "radius",
        [
            ("0"),
            ("LEROY"),
            ("JENKINS"),
        ],
    )
    def test_area_invalid_input(self, radius):
        # when + then
        with pytest.raises(TypeError):
            area(radius)

    # given
    @pytest.mark.parametrize(
        "radius, expected",
        [
            (0, 0),
            (1, 6.283185307179586),
            (5, 31.41592653589793),
        ],
    )
    def test_perimeter_valid_input(self, radius, expected):
        # when
        actual = perimeter(radius)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "radius",
        [
            ("0problems"),
            ("LEROY"),
            ("\n"),
        ],
    )
    def test_perimeter_invalid_input(self, radius):
        # when + then
        with pytest.raises(ValueError):
            perimeter(radius)
