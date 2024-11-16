import pytest
import sys

sys.path.append("../")
from geometric_lib.calculate import calc


class TestCalculate:
    # given
    @pytest.mark.parametrize(
        "fig, func, radius, expected",
        [
            ("circle", "area", 5, 78.53981633974483),
            ("circle", "area", 1, 3.141592653589793),
            ("circle", "area", 0, 0),
        ],
    )
    def test_calc_valid_circle_area(self, fig, func, radius, expected):
        # when
        actual = calc(fig, func, radius)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "fig, func, radius",
        [
            ("circle", "area", "oas"),
            ("circle", "area", "None"),
            ("circle", "area", "PLUH"),
        ],
    )
    def test_calc_invalid_circle_area(self, fig, func, radius):
        # when + then
        with pytest.raises(TypeError):
            calc(fig, func, radius)

    # given
    @pytest.mark.parametrize(
        "fig, func, radius, expected",
        [
            ("circle", "perimeter", 2, 12.566370614359172),
            ("circle", "perimeter", 1, 6.283185307179586),
            ("circle", "perimeter", 0, 0),
        ],
    )
    def test_calc_valid_circle_perimeter(self, fig, func, radius, expected):
        # when
        actual = calc(fig, func, radius)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "fig, func, radius",
        [
            ("circle", "perimeter", "PLUH"),
            ("circle", "perimeter", "PLU"),
            ("circle", "perimeter", "\n"),
        ],
    )
    def test_calc_invalid_circle_perimeter(self, fig, func, radius):
        # when + then
        with pytest.raises(TypeError):
            calc(fig, func, radius)

    # given
    @pytest.mark.parametrize(
        "fig, func, radius, expected",
        [
            ("circle", "area", -5, None),
            ("circle", "area", -12, None),
            ("circle", "perimeter", -15, None),
        ],
    )
    def test_calc_invalid_size_circle(self, fig, func, radius, expected):
        # when
        actual = calc(fig, func, radius)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "fig, func, side, expected",
        [
            ("square", "area", 4, 16),
            ("square", "area", 0, 0),
            ("square", "area", 1, 1),
        ],
    )
    def test_calc_valid_square_area(self, fig, func, side, expected):
        # when
        actual = calc(fig, func, side)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "fig, func, side",
        [
            ("square", "area", "pluh"),
            ("square", "area", "\n"),
            ("square", "area", "§"),
        ],
    )
    def test_calc_invalid_square_area(self, fig, func, side):
        # when + then
        with pytest.raises(TypeError):
            calc(fig, func, side)

    # given
    @pytest.mark.parametrize(
        "fig, func, side, expected",
        [
            ("square", "perimeter", 4, 16),
            ("square", "perimeter", 1, 4),
            ("square", "perimeter", 0, 0),
        ],
    )
    def test_calc_valid_square_perimeter(self, fig, func, side, expected):
        # when
        actual = calc(fig, func, side)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "fig, func, side",
        [
            ("square", "perimeter", "\n"),
            ("square", "perimeter", "YOLO"),
            ("square", "perimeter", " "),
        ],
    )
    def test_calc_valid_square_perimeter(self, fig, func, side):
        # when + then
        with pytest.raises(TypeError):
            calc(fig, func, side)

    # given
    @pytest.mark.parametrize(
        "fig, func, side, expected",
        [
            ("square", "area", -5, None),
            ("square", "perimeter", -12, None),
            ("square", "area", -15, None),
        ],
    )
    def test_calc_invalid_size_square(self, fig, func, side, expected):
        # when
        actual = calc(fig, func, side)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "fig, func, side_1, side_2, side_3, expected",
        [
            ("triangle", "area", 3, 4, 5, 6),
            ("triangle", "area", 5, 12, 13, 30),
            ("triangle", "area", 0, 0, 0, 0),
        ],
    )
    def test_calc_valid_triangle_area(
        self, fig, func, side_1, side_2, side_3, expected
    ):
        # when
        actual = calc(fig, func, side_1, side_2, side_3)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "fig, func, side_1, side_2, side_3",
        [
            ("triangle", "area", "g", "d", "r"),
            ("triangle", "area", "PLUH", 12, 13),
            ("triangle", "area", 0, 0, "iao"),
        ],
    )
    def test_calc_invalid_triangle_area(self, fig, func, side_1, side_2, side_3):
        # when + then
        with pytest.raises(TypeError):
            calc(fig, func, side_1, side_2, side_3)

    # given
    @pytest.mark.parametrize(
        "fig, func, side_1, side_2, side_3, expected",
        [
            ("triangle", "perimeter", 3, 4, 5, 12),
            ("triangle", "perimeter", 1, 1, 1, 3),
            ("triangle", "perimeter", 0, 0, 0, 0),
        ],
    )
    def test_calc_valid_triangle_perimeter(
        self, fig, func, side_1, side_2, side_3, expected
    ):
        # when
        actual = calc(fig, func, side_1, side_2, side_3)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "fig, func, side_1, side_2, side_3",
        [
            ("triangle", "perimeter", "3", "U", "5"),
            ("triangle", "perimeter", "\n", "\n", "\n"),
            ("triangle", "perimeter", "\nHELLO", "\nWOLRD!!!", "\nYOLO"),
        ],
    )
    def test_calc_invalid_triangle_perimeter(self, fig, func, side_1, side_2, side_3):
        # when + then
        with pytest.raises(TypeError):
            calc(fig, func, side_1, side_2, side_3)

    # given
    @pytest.mark.parametrize(
        "fig, func, side_1, side_2, side_3, expected",
        [
            ("triangle", "area", -5, -3, 4, None),
            ("triangle", "area", 52, -52, 52, None),
            ("triangle", "perimeter", -1, -1, 1, None),
        ],
    )
    def test_calc_invalid_size_triangle(
        self, fig, func, side_1, side_2, side_3, expected
    ):
        # when
        actual = calc(fig, func, side_1, side_2, side_3)

        # then
        assert actual == expected

    # given
    @pytest.mark.parametrize(
        "fig, func, side_1, side_2, side_3, expected",
        [
            ("triangle", "area", 1, 2, 4, None),
            ("triangle", "perimeter", 1, 2, 83, None),
            ("triangle", "area", 3, 2, 14, None),
        ],
    )
    def test_calc_triangle_impossible_sides(
        self, fig, func, side_1, side_2, side_3, expected
    ):
        # when
        actual = calc(fig, func, side_1, side_2, side_3)

        # then
        assert actual == expected
