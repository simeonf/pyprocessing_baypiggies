from pyprocessing import *
import cPickle as pickle

data = pickle.load(open("zipcodes.bin"))
prefix = ''
font = None
red_img = None
yellow_img = None

def setup():
    global font, red_img, yellow_img
    size(800,600) # create a window
    font = createFont("Times New Roman", 24)
    # This takes a very long time!
    # 0.1.3 uses numpy for PImage, faster than 0.1.2 arrays, still slow
    red_img = loadImage("red.png")
    yellow_img = loadImage("yellow.png")
    textFont(font)
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
    # Simple case: show precached image
    if not prefix:
        image(yellow_img, 0, 0)
        return

    # Else - show red image and put yellow points on top
    image(red_img, 0, 0)
    yellow = color(240, 240, 100)
    stroke(yellow)
    if len(prefix) == 1: # no .startswith
         prefix_zips = (z for z in data[prefix[0]])
    else:
        prefix_zips = (z for z in data[prefix[0]] if z[0].startswith(prefix))
    for zipcode in prefix_zips:
        point(zipcode[1], zipcode[2])
    # Show the zipcode prefix
    text(prefix, 15, 30)

if __name__ == '__main__':
    run()    
    
