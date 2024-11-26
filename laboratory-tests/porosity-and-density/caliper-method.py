from math import pi

#diameter and the length of the specimen is used
def bulk_volume(diameter, length):
    area = pi * (diameter)**2
    bv = area * length
    return bv