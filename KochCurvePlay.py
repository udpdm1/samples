'''
Code sample borrowed from web to understand regressive functions.
See original article: https://python-with-science.readthedocs.io/en/latest/koch_fractal/koch_fractal.html
'''
# Draw a Koch snowflake
from turtle import *

def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3, order-1)
            left(t)
    else:
        forward(a)

def main():
    # Test
    #koch(100, 1)

    # Choose colors and size
    color("sky blue", "white")
    bgcolor("black")
    size = 400
    order = 7

    # Ensure snowflake is centered
    penup()
    backward(size/1.732)
    left(30)
    pendown()

    # Make it fast

    tracer(100)
    hideturtle()

    begin_fill()

    # Three Koch curves

    for i  in range(3):
        koch(size, order)
        right(120)

    end_fill()

    # Make the last parts appear
    update()

    result = input('PRESS ANY KEY TO CONTINUE: ')

if __name__ == "__main__":
    #run the script and called functions
    main()
 
