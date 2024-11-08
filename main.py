"""
programme main
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Ce programme permet de renvoyer true si le nombre entrer en paramètre est premier 
    sinon il renvoie false
    """

    rac = sqrt(p)
    racine = int(rac)
    premier = True
    if p==1:
        return False
    for i in range (2,racine+1):
        if p%i==0 :
            premier = False
            break
    return premier

#### Fonction principale


def main():
    """
    permet d'appeler la fonction pour tester sur les 100 premiers nombres
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime (n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
