from figures.circle import area as circle_area, perimeter as circle_perimeter
from figures.triangle import area as triangle_area, perimeter as triangle_perimeter
from figures.square import area as square_area, perimeter as square_perimeter

# List of available figures and functions
figs = ["circle", "square", "triangle"]
funcs = ["perimeter", "area"]
sizes = {}  # Dictionary to store expected sizes for figure-function combinations


def calc(fig, func, *args):
    """
    Calculate the specified function (perimeter or area) for a given figure (circle or square).

    Parameters:
        fig (str): The figure type ('circle' or 'square').
        func (str): The function to calculate ('perimeter' or 'area').
        size (list): A list of sizes needed for the calculation (e.g., radius for circle, side length for square).

    Return value:
        float: The calculated area or perimeter of the specified figure.
                Returns None if the input parameters are invalid.

    Example:
        calc('circle', 'area', [1])
                invokes the 'circle' module
                        invokes the 'area' function
                                area(1)
                        (pi * 1 * 1) = pi
                        returns (pi) ≈ 3.1415926535...

    """
    # Check if figures and functions are valid
    if fig not in figs:
        return None
    if func not in funcs:
        return None

    functions = {
        "circle": {
            "area": circle_area,
            "perimeter": circle_perimeter,
        },
        "square": {
            "area": square_area,
            "perimeter": square_perimeter,
        },
        "triangle": {
            "area": triangle_area,
            "perimeter": triangle_perimeter,
        },
    }

    # Get result from functions
    # If there are less than 3 sides given to triangle, return None
    if fig == "triangle" and func == "area":
        if len(args) != 3:
            return None

    # If there are negative arguments, return None
    if any(num < 0 for num in args):
        return None

    # If sides of triangle are impossible, return None
    if fig == "triangle":
        sides = args
        if (
            (sides[0] + sides[1] < sides[2])
            or (sides[0] + sides[2] < sides[1])
            or (sides[2] + sides[1] < sides[0])
        ):
            return None

    # If got triangle, evaluate given function to it
    if fig == "triangle":
        sides = args
        result = functions[fig][func](sides[0], sides[1], sides[2])
        return result

    # Else, evaluate other stuff
    size = args[0]
    result = functions[fig][func](size)
    return result

if __name__ == "__main__":  # Check if calculate.py is running or imported
    func = ""  # Initialize function
    fig = ""  # Initialize figure
    size = list()  # Initialize size list
    number_of_commands = 1

    # Ask user for figure until he gets it right
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    # Ask user for function until he gets it right
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    if fig == "triangle":
        number_of_commands = 3

    # Ask user for size number until he gets it right
    while len(size) != number_of_commands:
        user_input = input(
            "Input figure sizes separated by space, 1 for circle and square\n"
        )
        try:
            values = user_input.split(" ")
            numbers = [int(value) for value in values]
            size = numbers
        except ValueError:
            print("Invalid sizes!")

    # Calculate user's data
    data = calc(fig, func, size)
    print(f"{func} of {fig} is {data}")
