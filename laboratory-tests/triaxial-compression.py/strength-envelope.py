from math import sin, cos, acos, asin

#m->gradient of the strength envelope
#b->Y intercept of the strength envelope
def internal_friction_angle(m):
    fi = asin((m-1)/(m+1))
    return fi