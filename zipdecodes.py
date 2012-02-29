from pyprocessing import *

# Data consists of four columns: zip, orthoX, orthoY, place name in tab separated file
data = (l.strip("\n").split("\t") for l in open("./zipcodes.csv", "r"))
# Go ahead and convert orthographic projections to floats
data = [(l[0], float(l[1]), float(l[2]), l[3]) for l in data]
cols = zip(*data)
min_x = min(cols[1])
max_x = max(cols[1])
min_y = min(cols[2])
max_y = max(cols[2])

prefix = ''
font = None

def setup():
    global font
    size(800,600) # create a window
    font = createFont("Times New Roman", 24)
    textFont(font)
    smooth() # turn on anti-aliasing
    noLoop() # don't call the draw function repeatedly

def keyPressed():
    """Event handler for keypresses, auto called by processing. 
    Only redraw the screen when there's been valid data input."""
    
    global prefix
    if key.char and key.char.isdigit():
        prefix = prefix + key.char
        redraw()
    elif key.code == BACKSPACE:
        prefix = prefix[:-1]
        redraw()
    

def draw():
    background(0) # Paint the whole screen black
    yellow = color(240, 240, 100) # add some colors
    red = color(240, 0, 0)
    for zipcode in data:
        if prefix and not zipcode[0].startswith(prefix):
            pnt_color = red # zipcodes not in our partial zip 
        else:
            pnt_color = yellow 
        coords = (int(map(zipcode[1], min_x, max_x, 50, 750)),
                 int(map(zipcode[2], max_y, min_y, 50, 550)))
        stroke(pnt_color)
        point(*coords)
    # Show the zipcode prefix if any
    if prefix:
        fill(yellow)
        text(prefix, 15, 30)
    
if __name__ == '__main__':
    run()    
    
