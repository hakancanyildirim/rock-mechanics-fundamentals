from math import cos, sin, tan

#tau->shear stress
#i->angle of incidence of the projections
#sigma->normal stress
#taum->shear stress on the sheared plane
def shear_stress_on_sheared_plane(tau, i, sigma):
    taum = tau*cos(i)-sigma*sin(i)
    return taum

#tau->shear stress
#i->angle of incidence of the projections
#sigma->normal stress
#sigmam->normal stress on the sheared plane
def normal_stress_on_sheared_plane(tau, i, sigma):
    sigmam = tau*sin(i)+sigma*cos(i)
    return sigmam

#taum->shear stress on the sheared plane
#sigmam->normal stress on the sheared plane
#fi->basic friction angle of the material
def shear_stress_and_normal_stress_relation(sigmam, fi):
    taum = sigmam*tan(fi)
    return taum

#sigma->normal stress
#fi->basic friction angle of the material
#i->angle of incidence of the projections
def substition_of_shear_and_normal_stresses(sigma, fi, i):
    tau = sigma*tan(fi+i)
    return tau

#c->apparent cohesion at a stress level corresponding to fi(b)
#sigma->normal stress
#fi->basic friction angle of the material
def shear_strength(c, sigma, fi):
    tau = c+sigma*tan(fi)
    return tau
