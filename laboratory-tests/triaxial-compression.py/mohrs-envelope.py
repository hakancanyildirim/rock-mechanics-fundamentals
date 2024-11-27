from math import tan, sin, cos

#C->cohesion
def linear_mohrs_envelope_ucs(c, fi):
    sigmac = (2*c*cos(fi))/(1-sin(fi))
    return sigmac
