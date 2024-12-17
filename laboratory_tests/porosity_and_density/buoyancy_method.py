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

#gw->mineral grain weight
#bv->bulk volume
def dry_density(gw, bv):
    µd = gw/bv
    return µd

#wsat->saturated weight
#bv->bulk volume
def saturated_density(wsat, bv):
    µsat = wsat/bv
    return µsat

#wsat->saturated weight
#wsub->submerged weight
#pw->density of water
def bulk_volume(wsat, wsub, pw):
    bv = (wsat-wsub)/pw
    return bv
