#p1->weight of pycnometer
#p2->weight of pycnometer + sample
#p3->weight of pycnometer + water + sample
#p4->weight of pycnometer + water
#dw->density of water
def mineral_grain_density(p1,p2,p3,p4,dw):
    mgd = ((p2-p1)*dw)/(p4+p2-p1-p3)
    return mgd

#mg->mineral grain density
#md->dry density
def total_porosity_percentage(mg,md):
    tp = ((mg-md)/mg)*100
    return tp