
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square, Triangle.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square, three sides for triangle.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Square: `S = a²`
- Triangle: `S = (a + h) / 2`

## Perimeter
- Circle: `P = 2πR`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Description
This project is a simple calculator for calculating the area and perimeter of geometric shapes such as circles and squares.

The user enters the name of the shape, selects what needs to be calculated (area or perimeter), and enters the necessary dimensions, for example, radius for a circle or side for a square. 

The program uses ready-made mathematical formulas for calculations and outputs the result directly on the command line. 

The main goal of the project is to simplify calculations for the user by providing a simple and intuitive interface.

# Functions and their descriptions, with example
## `calculate.py`
### `def calc(fig, func, size):`
- Calculates for the chosen figure, chosen function
- Example of a call:
```python
>> calc('circle', 'area', [1])
3.14159265358979 
```
## `circle.py`
### `def area(r):`
- Calculates the area of a circle.
- Example of a call:
```python
>> area(1)
3.14159265358979 
```
### `def perimeter(r):`
- Calculates the perimeter of a circle
- Example of a call:
```python
>> perimeter(1)
6,28318530718
```
## `square.py`
### `def area(a):`
- Calculates the area of a square
- Example of a call:
```python
>> area(5)
25
```
### `def perimeter(a):`
- Calculates the perimeter of a square
- Example of a call:
```python
>> perimeter(5)
20
```
## `triangle.py`
### `def area(a):`
- Calculates the area of a triangle
- Example of a call:
```python
>> area(4, 4)
4.0
```
### `def perimeter(a):`
- Calculates the perimeter of a triangle 
- Example of a call:
```python
>> perimeter(4, 4, 4)
12.0
```

# History of changes

1. **875381f** - Petruha: Added a documentation for calculate
   Added documentation for `calculate.py` file

2. **94c2627** - Petruha: Added a documentation for triangle and fixed area calculation
   Added documentation for working with triangles and fixed calculation of area of a triangle

3. **22fe560** - Petruha: Added a documentation for square
   Added documentation for working with squares

4. **2708f04** - Petruha: Added a documentation for circle
   Added documentation for working with circles

5. **d76db2a** - L-04: Add calculate.py  
   Added the `calculate.py` file for performing calculations.

6. **51c40eb** - L-04: Doc updated for triangle  
   Updated documentation for working with triangles.

7. **d080c78** - L-04: Triangle added  
   Added functionality for working with triangles.

8. **8ba9aeb** - L-03: Circle and square added  
   Added functions for working with circles and squares.
