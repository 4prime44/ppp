import random

def generuj_kod(dlugosc=4,zakres_cyfr=(1,9),powtorzenia=True):
    min_cyfra,max_cyfra = zakres_cyfr
    dostepne_cyfry=list(range(min_cyfra,max_cyfra+1))
    if powtorzenia:
        return random.choices(dostepne_cyfry, k=dlugosc)
    else:
        if dlugosc > len(dostepne_cyfry):
            raise ValueError("za dlugie")
        return random.sample(dostepne_cyfry,dlugosc)