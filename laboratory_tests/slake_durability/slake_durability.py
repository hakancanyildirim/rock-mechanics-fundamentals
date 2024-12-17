#d->mass of drum
#a->mass of drum + sample
#b->mass of drum + retained sample
#c->mass of drum + retained sample
def slake_durability(d, a, b, c):
    classification = None
    id1 = ((b-d)/(a-d))*100
    id2 = ((c-d)/(a-d))*100
    if 0<=id1<=25 or 0<=id2<=25:
        classification = "Very Low"
    elif 25<id1<=50 or 25<id2<=50:
        classification = "Low"
    elif 50<id1<=75 or 50<id2<=75:
        classification = "Medium"
    elif 75<id1<=90 or 75<id2<=90:
        classification = "High"
    elif 90<id1<=95 or 90<id2<=95:
        classification = "Very High"
    elif 95<id1<=100 or 95<id2<=100:
        classification = "Extremely High"
    return classification
