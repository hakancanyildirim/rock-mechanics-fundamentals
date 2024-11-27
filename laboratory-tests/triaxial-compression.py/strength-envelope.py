from math import sin, cos, acos, asin

#m->gradient of the strength envelope
def internal_friction_angle(m):
    fi = asin((m-1)/(m+1))
    return fi

#fi->internal friction angle
#b->Y intercept of the strength envelope
def cohesion(fi, b):
    c = b*((1-sin(fi))/(2*cos(fi)))
    return c