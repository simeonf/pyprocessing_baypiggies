from pyprocessing import *
from demographics_loading import Sequence, interpolate

data = [l.strip("\n").split(",") for l in open("./data.csv", "r")]
# Data consists of first column year, next paired columns data per country
#Year, Country1 A, Country1 B, Country2 A, Country2 B, etc

countries = [col for col in data[0][1:] if col]
colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]
s = Sequence(countries, colors, data[1:])

frames = 40 # Number of frames a year lasts


def setup():
    size(800,600) # create a window
    smooth() # turn on anti-aliasing
    noStroke() # I'll just draw shapes w/o edges

def draw():
    i = frame.count / frames # frameCount in java -> frame.count
    if i >= s.length - 1: # If we're on the last frame 
        return
    
    background(204) # Paint the whole screen grey every loop
    partial = frame.count % frames # How far through the current year animation are we
    r = s.data[i] # Get current row of data
    for c in countries:
        fill(*(r[c].color + (50,))) # set the fill color for this country with 50% alpha
        data = (r.x, r[c].a, r[c].b, r[c].b)
        if partial and i < s.length - 1: # If partway to next step
            percent = partial / float(frames) 
            r2 = s.data[i + 1] # Get next data set
            data2 = (r2.x, r2[c].a, r2[c].b, r2[c].b)
            data = interpolate(data, data2, percent) # Currently drawing interpolated data
        ellipse(*data)
    
if __name__ == '__main__':
    run()    
    
