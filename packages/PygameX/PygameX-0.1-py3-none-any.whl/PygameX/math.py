import math as mth

def distance_to(p1, p2):
    k1 = p1[0] - p2[0]
    k2 = p1[1] - p2[1]
    return mth.sqrt( (k1*k1) + (k2*k2) )
