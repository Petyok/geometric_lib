'''Import for pi'''
import math


def area(r):
    '''
    Calculates the area of a circle.
    
        Parameters:
            r (int): radius of a circle.
        
        Return value:
            (float) : the area of a circle.

        Example:
            area(1)
            (pi * 1 * 1) = pi
            returns (pi) ≈ 3.14159265358979 

    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Calculates the perimeter of a circle.
    
        Parameters:
            r (int): radius of a circle.
        
        Return value:
            (float) : the area of a circle.
        
        Example:
            perimeter(1)
            (2 * pi * 1) = (2 * pi)
            returns (2 * pi) ≈ 6,28318530718

    '''
    return 2 * math.pi * r

