def area(a, h):
    '''
    Calculates the area of a triangle.
    
        Parameters:
            a (int): base of the triangle.
            h (int): height of the triangle
        
        Return value:
            (int) : the area of a triangle.

        Example:
            area(4, 4)
            [ (4 + 4) / 2 ] = 4
            returns 4

    '''
    return (a + h) / 2


def perimeter(a, b, c):
    '''
    Calculates the perimeter of a triangle.
    
        Parameters:
            a (int): side of a triangle.
            b (int): side of a triangle.
            c (int): side of a triangle.
        
        Return value:
            (int) : the perimeter of a triangle.

        Example:
            perimeter(4, 4, 4)
            (4 + 4 + 4) = 12
            returns 12
    '''    
    return a + b + c
