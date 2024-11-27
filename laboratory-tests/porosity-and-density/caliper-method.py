from math import pi

#diameter and the length of the specimen is used
def bulk_volume(diameter, length):
    area = pi * (diameter)**2
    bv = area * length
    return bv

#pv->pore volume
#bv->bulk volume
def effective_porosity(pv, bv):
    n = (pv/bv)*100
    return n

#wsat->saturated weight
#gw->mineral grain weight
#pw->density of water
def pore_volume(wsat, gw, pw):
    pv = (wsat-gw)/pw
    return pv