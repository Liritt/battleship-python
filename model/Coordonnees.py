# Coordonnees.py

#
# - Définit les coordonnées d'une case
#
#  Une coordonnée est un tuple de deux entiers compris entre 0 (inclus) et const.DIM (exclus)
#  Elle peut aussi être None si elle est non définie
#

from model.Constantes import *


def type_coordonnees(c: tuple) -> bool:
    """
    Détermine si le tuple correspond à des coordonnées
    Les coordonnées sont sous la forme (ligne, colonne).
    Malheureusement, il n'est pas possible de tester si une inversion est faite entre ligne et colonne...

    :param c: coordonnées
    :return: True s'il s'agit bien de coordonnées, False sinon
    """
    return c is None or (type(c) == tuple and len(c) == 2 and 0 <= c[0] < const.DIM and 0 <= c[1] < const.DIM)


def sontVoisins(coord1: tuple, coord2: tuple) -> bool:
    voisins = False
    if coord1 == None or not type_coordonnees(coord1):
        raise ValueError(f'sontVoisins : le paramètre {coord1} n’est pas de type coordonnées')
    if coord2 == None or not type_coordonnees(coord2):
        raise ValueError(f'sontVoisins : le paramètre {coord2} n’est pas de type coordonnées')
    y, x = coord1
    lst = []
    lst.append((y - 1, x))
    lst.append((y, x - 1))
    lst.append((y - 1, x - 1))
    lst.append((y + 1, x - 1))
    lst.append((y - 1, x + 1))
    lst.append((y + 1, x))
    lst.append((y, x + 1))
    lst.append((y + 1, x + 1))
    return coord2 in lst





