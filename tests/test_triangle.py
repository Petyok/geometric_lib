import pytest
from ..figures.triangle import area, perimeter
from math import sqrt


class TestTriangle:
    # given
    @pytest.mark.parametrize(
        "a, b, c, expected", [(3, 4, 5, 6), (5, 12, 13, 30), (7, 24, 25, 84)]
    )
    def test_area_valid_input(self, a, b, c, expected):
        # when
        actual = area(a, b, c)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize("a, b, c", [(3, "yolo", 0), (0, "\n", 0), (0, "", 0)])
    def test_area_invalid_input(self, a, b, c):
        # when + then
        with pytest.raises(TypeError):
            area(a, b, c)

    # given
    @pytest.mark.parametrize(
        "a, b, c, expected", [(1, 2, 3, 6), (0, 0, 0, 0), (1.2, 2.4, 2.4, 6)]
    )
    def test_perimeter_valid_input(self, a, b, c, expected):
        # when
        actual = perimeter(a, b, c)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "a, b, c", [(0, 0, "bazinga"), (4, "\n", "\n"), (4, 2, "3")]
    )
    def test_perimeter_invalid_input(self, a, b, c):
        # when + then
        with pytest.raises(TypeError):
            perimeter(a, b, c)
