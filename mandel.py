from pyprocessing import *

# The four points of the box on the argand plane I want to look at
# Screen is 800x600 or 4x3 in proportion so
x_min = -3
x_max = x_min + 4
y_min = -1.5
y_max = y_min + 3

def mandel(c):
    """
    Returns true if complex number is in mandelbrot set.

    The mandelbrot set is drawn by looking at a number 'c' in the
    argand plane (2d space where x=real numbers, y=imaginary) and
    testing by function z=z**2 + c where z starts at zero. If after
    number of iterations z remains close to c than c is a stable
    number and is a member, if z increases infinitely it is not a
    member.

    http://prezjordan.tumblr.com/post/277984651/mandelbrot-set-in-python
    """
    z=0
    for h in range(0,20):
        z = z**2 + c
        if abs(z) > 2:
            break
    if abs(z) >= 2:
        return (False, h)
    else:
        return (True, None)


def setup():
    size(800,600) # create a window
    smooth() # turn on anti-aliasing
    noLoop() # don't call the draw function repeatedly


def mouseClicked():
    """When you click - center the viewport on the click and the box
    should be 80% as large as current box."""
    global x_min, x_max, y_min, y_max
    print((map(mouse.x, 0, 800, x_min, x_max), map(mouse.y, 0, 600, y_min, y_max)))
    x_margin = (x_max - x_min) * 0.2
    y_margin = (y_max - y_min) * 0.2
    x_min = x_min + x_margin
    x_max = x_max - x_margin
    y_min = y_min + y_margin
    y_max = y_max - y_margin
    redraw()


def draw():
    """Naive - do 800 in real, 600 in imaginary"""
    background(0) # Paint the whole screen black
    red = color(240, 0, 0)
    black = color(0, 0, 0)
    white = color(255, 255, 255)
    for r in xrange(0, 800, 1):
        for i in xrange(0, 600, 1):
            # Given pixels, map to box in argand plane
            p = complex(map(r, 0, 800, x_min, x_max),
                        map(i, 600, 0, y_min, y_max)) #pyprocessing draws +y downwards on screen
            (in_set, num_iterations) = mandel(p)
            if in_set:
                stroke(red)
                point(r, i)
            else:
                stroke(lerpColor(black, white, map(num_iterations, 0, 19, 0, 1)))
                point(r, i)


if __name__ == '__main__':
    run()

