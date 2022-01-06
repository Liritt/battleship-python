# Grille.py

from model.Constantes import *
from model.Case import type_case
from model.Joueur import setEtatSegmentBateau
from model.Coordonnees import type_coordonnees

#
# - Définition de la grille des tirs
#       - tableau 2D (const.DIM x const.DIM) contenant des cases de type type_case.
#
# Bien qu'on pourrait créer une autre grille contenant les bateaux, ceux-ci seront stockés dans une liste
# et chaque bateau contiendra sa liste de coordonnées.
#


def type_grille(g: list) -> bool:
    """
    Détermine si le paramètre est une grille de cases dont le type est passé en paramètre ou non
    :param g: paramètre à tester
    :return: True s'il peut s'agir d'une grille du type voulu, False sinon.
    """
    res = True
    if type(g) != list or len(g) != const.DIM:
        res = False
    else:
        i = 0
        while res and i < len(g):
            res = type(g[i]) == list and len(g[i]) == const.DIM
            j = 0
            while res and j < len(g[i]):
                res = type_case(g[i][j])
                j += 1
            i += 1
    return res


def construireGrille() -> list:
    lst = []
    for y in range(const.DIM):
        lst.append([None]*const.DIM)
    return lst


def marquerCouleGrille(grille: list, coord: tuple) -> None:
    if not type_grille(grille):
        raise ValueError(
            f"marquerCouleGrille: Ceci {grille} n'est pas une grille")
    if not type_coordonnees(coord):
        raise ValueError(
            f"marquerCouleGrille: les valeurs {coord} ne correspondent pas à des coordonnées")
    lst = []
    lst.append(coord)
    while len(lst) != 0:
        coord = lst.pop()
        grille[coord[0]][coord[1]] = const.COULE
        if coord[0] > 0 and grille[coord[0] - 1][coord[1]] == const.TOUCHE:
            lst.append((coord[0] - 1, coord[1]))
        if coord[0] < len(grille[0]) - 1 and grille[coord[0] + 1][coord[1]] == const.TOUCHE:
            lst.append((coord[0] + 1, coord[1]))
        if coord[1] > 0 and grille[coord[0]][coord[1] - 1] == const.TOUCHE:
            lst.append((coord[0], coord[1] - 1))
        if coord[1] < len(grille[0]) - 1 and grille[coord[0]][coord[1] + 1] == const.TOUCHE:
            lst.append((coord[0], coord[1] + 1))

