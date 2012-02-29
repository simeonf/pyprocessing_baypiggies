"""Utility classes for loading demographic data. Pure python, no
pyprocessing api calls."""

class Record(dict):
    """Convenience class to access dict by . operator."""
    
    def __getattr__(self, name):
        return self[name]
    
    def __str__(self):
        return str(self.__dict__)

def interpolate(current, next, percentage):
    """Given two tuples of integer data points return a new data tuple
    percentage between.
    
    >>> interpolate((1, 4, 9), (5, 12, 11), .5)
    (3, 8, 10)

    """

    new = []
    for i in range(len(current)):
        step = int((next[i] - current[i]) * percentage)
        new.append(current[i] + step)
    return tuple(new)
    
def normalize_r(val, min=0, max=100, scale=600, flip=False):
    """Adjust a number to fit on a scale. Eg for numbers 0, 100 with a scale of 800
    100 should be 800, 0 should be 0, and 50 should be 400.

    Just realized that processing includes a "map" function.

    >>> normalize_r(0)
    0
    >>> normalize_r(40)
    240
    >>> normalize_r(1930, min=1900, max=1950)
    360
    """
    val = val - min # adjust for starting point
    val = val / float(max-min) # get as percentage of max-min range
    val = int(val * scale) # return as percentage of scale
    if flip:
        val = scale - val
    return val
    
    
class Sequence(object):
    """Handle loading of data points by countries by year. Create a
    series of records with data normalized to fit on expected graph.
    """
    def __init__(self, countries, colors, data):
        self.data = []
        self.years = []
        max_x = len(data)
        for y, row in enumerate(data):
            r = Record(year=int(row[0]), x=normalize_r(y, max=max_x, scale=800))
            for x, country in enumerate(countries):
                step = x * 2
                r[country] = Record(a=normalize_r(int(row[1 + step]), max=50, flip=True),
                                    b= 10 * int(row[2 + step]),
                                    color=colors[x])
            self.data.append(r)
    def __str__(self):
        return str(self.data)
    
    @property
    def length(self):
        return len(self.data)
