def sum(a, b):
    return a+b


def moyenne_liste(liste):
    somme = 0
    for i in liste:
        somme += i
    return somme/len(liste)
