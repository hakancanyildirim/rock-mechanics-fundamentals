#fc->cohesion force
#a->area
#p->
def principal_stresses(fc, a, p):
    sigma1 = fc/a
    sigma2, sigma3 = p
    return sigma1, sigma2, sigma3 

