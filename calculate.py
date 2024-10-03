import circle  
import square  

# List of available figures and functions
figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}  # Dictionary to store expected sizes for figure-function combinations

def calc(fig, func, size):
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
	# check if figures and functions are valid
    assert fig in figs  
    assert func in funcs 

    # Evaluate the function call for the figure and function
    result = eval(f'{fig}.{func}(*{size})')
	# print result
    print(f'{func} of {fig} is {result}')

if __name__ == "__main__": # check if calculate.py is running or imported
    func = ''  # Initialize function 
    fig = ''   # Initialize figure 
    size = list()  # Initialize size list
    
    # Ask user for figure until he gets it right
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    # Ask user for function until he gets it right
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    # Ask user for size number until he gets it right
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    
    # Calculate user's data
    calc(fig, func, size)