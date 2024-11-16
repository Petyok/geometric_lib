import pytest
from geometric_lib.figures.square import area, perimeter


class TestSquare:
    # given
    @pytest.mark.parametrize(
        "side, expected",
        [
            (5, 25),
            (1, 1),
            (0, 0),
        ],
    )
    def test_area_valid_input(self, side, expected):
        # when
        actual = area(side)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "side",
        [
            ("$@"),
            ("Engineer gaming"),
            ("LER"),
        ],
    )
    def test_area_invalid_input(self, side):
        # when + then
        with pytest.raises(TypeError):
            area(side)

    # given
    @pytest.mark.parametrize(
        "side, expected",
        [
            (5, 20),
            (1, 4),
            (0, 0),
        ],
    )
    def test_perimeter_valid_input(self, side, expected):
        # given
        side = 5
        expected = side * 4

        # when
        actual = perimeter(side)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "side",
        [
            ("$@"),
            ("Engineer gaming"),
            ("LER"),
        ],
    )
    def test_perimeter_invalid_input(self, side):
        # when + then
        with pytest.raises(ValueError):
            perimeter(side)
