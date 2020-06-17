#Arthur : Eugene Parker 

from math import pi

def surfaceArea(radius):
    f = 4 * pi * (radius ** 2)
    return f

def sphereVolume(radius):
    g = (4/3) * (pi * (radius ** 3))
    return g

def main():
    radius = 1
    area = surfaceArea(radius)
    volume = sphereVolume(radius)

    print("Area: {}".format(area))
    print("Volume: {}".format(volume))
