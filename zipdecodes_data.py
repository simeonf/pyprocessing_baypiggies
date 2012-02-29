"""Write data file of preprocessed zipcode, pixelspace pairs from input csv."""
import cPickle as pickle
from pyprocessing import *

# Data consists of four columns: zip, orthoX, orthoY, place name in tab separated file
data = (l.strip("\n").split("\t") for l in open("./zipcodes.csv", "r"))
# Go ahead and convert orthographic projections to floats, discarding place name
data = [(l[0], float(l[1]), float(l[2])) for l in data]
cols = zip(*data)
min_x = min(cols[1])
max_x = max(cols[1])
min_y = min(cols[2])
max_y = max(cols[2])

# Now convert to pixel space
data = [(l[0], int(map(l[1], min_x, max_x, 50, 750)),
         int(map(l[2], max_y, min_y, 50, 550)),) for l in data]

# But we have many duplicates in pixel space. Do we need them?
points_seen = []
def dup_detector(row):
    pixels = (row[1], row[2])
    if pixels not in points_seen:
        points_seen.append(pixels)
        return True
    else:
        return False

data = filter(dup_detector, data)

# and finally lets store the data in a dict with keys 0..9
# representing the appropriate segment of data
dct = {}
for i in range(0,10):
    newlst = []
    for zipcode in data:
        if zipcode[0].startswith(str(i)):
            newlst.append(zipcode)
    dct[str(i)] = newlst
    
pickle.dump(dct, open("zipcodes.bin", "w"), pickle.HIGHEST_PROTOCOL)

# Now create an all yellow and all red image to pre-cache common cases
canvas1 = createImage(800, 600, RGB)
canvas2 = createImage(800, 600, RGB)
yellow = color(240, 240, 100) 
red = color(240, 0, 0)
for zipcode in data:
    canvas1.set(zipcode[1], zipcode[2], yellow)
    canvas2.set(zipcode[1], zipcode[2], red)
canvas1.save('yellow.png')
canvas2.save('red.png')

