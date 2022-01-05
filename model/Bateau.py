# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#

from model.Coordonnees import type_coordonnees, sontVoisins
from model.Segment import construireSegment, getCoordonneesSegment, type_segment
from model.Constantes import *


def type_bateau(bateau: dict) -> bool:
    """
    Détermine si la liste représente un bateau

    :param bateau: Liste représentant un bateau
    :return: <code>True</code> si la liste contient bien un bateau, <code>False</code> sinon.
    """
    return type(bateau) == dict and \
        all([v in bateau for v in [const.BATEAU_NOM, const.BATEAU_SEGMENTS]]) and \
        type(bateau[const.BATEAU_NOM]) == str and \
        bateau[const.BATEAU_NOM] in const.BATEAUX_CASES and type(bateau[const.BATEAU_SEGMENTS]) == list and \
        len(bateau[const.BATEAU_SEGMENTS]) == const.BATEAUX_CASES[bateau[const.BATEAU_NOM]] and \
        all([type_segment(s) for s in bateau[const.BATEAU_SEGMENTS]])


def est_horizontal_bateau(bateau: dict) -> bool:
    """
    Retourne True si le bateau est horizontal, False si il est vertical.

    :param bateau:
    :return: True si le bateau est horizontal, False si il est vertical
    :raise ValueError si le bateau n'est pas placé ou s'il n'est ni vertical, ni horizontal
    """
    if not estPlaceBateau(bateau):
        raise ValueError(
            "est_horizontal_bateau: Le bateau n'est pas positionné")
    pos = getCoordonneesBateau(bateau)
    res = True
    if len(pos) > 1:
        # Horizontal : le numéro de ligne ne change pas
        res = pos[0][0] == pos[1][0]
        # On vérifie que le bateau est toujours horizontal
        for i in range(1, len(pos)):
            if (res and pos[0][0] != pos[i][0]) or (not res and pos[0][1] != pos[i][1]):
                raise ValueError(
                    "est_horizontal_bateau: Le bateau n'est ni horizontal, ni vertical ??")
    return res


def construireBateau(nomBateau: str) -> dict:
    if nomBateau not in const.BATEAUX_CASES.keys():
        raise ValueError(
            f'construireBateau: Le bateau qui répond au nom de "{nomBateau}" n\'existe pas')

    nbSegments = const.BATEAUX_CASES[nomBateau]

    bateau = {
        const.BATEAU_NOM: nomBateau,
        const.BATEAU_SEGMENTS: [construireSegment()
                                for segment in range(nbSegments)]
    }
    return bateau


def getNomBateau(bateau: dict) -> str:
    if not type_bateau(bateau):
        raise ValueError(
            f"getNomBateau: La valeur {bateau} n'est pas un bateau")
    nomBateau = bateau.get(const.BATEAU_NOM)
    return nomBateau


def getTailleBateau(bateau: dict) -> str:
    if not type_bateau(bateau):
        raise ValueError(
            f"getTailleBateau: La valeur {bateau} n'est pas un bateau")
    tailleBateau = len(bateau.get(const.BATEAU_SEGMENTS))
    return tailleBateau


def getSegmentsBateau(bateau: dict) -> list:
    if not type_bateau(bateau):
        raise ValueError(
            f"getSegmentsBateau: La valeur {bateau} n'est pas un bateau")
    listeSegments = bateau.get(const.BATEAU_SEGMENTS)
    return listeSegments


def getSegmentBateau(bateau: dict, n: object) -> dict:
    segment = []
    segments = getSegmentsBateau(bateau)
    if not type_bateau(bateau):
        raise ValueError(
            f"getSegmentBateau: La valeur {bateau} n'est pas un bateau")
    if type(n) == int:
        if not (0 <= n < len(bateau[const.BATEAU_SEGMENTS])):
            raise ValueError(
                f"getSegmentBateau: La valeur est en dehors des limites")
    elif type(n) == tuple:
        if not type_coordonnees(n):
            raise ValueError(
                f"getSegmentBateau : le paramètre {n} ne correspond pas à des coordonnées.")
        trouve = False
        i = 0
        while not trouve and i < len(segments):
            if getCoordonneesSegment(segments[i]) == n:
                trouve = True
                segment = segments[i]
            i += 1
        if not trouve:
            raise ValueError(f"getSegmentBateau : les coordonnées {n} sont introuvables dans ce bateau")
    else:
        raise ValueError(
            f"getSegmentBateau: Le type du second paramètre {type(n)} ne correspond pas...")
    return segment if type(n) == tuple else bateau[const.BATEAU_SEGMENTS][n]


def setSegmentBateau(bateau: dict, numSeg: int, segmt: dict) -> dict:
    if not type_bateau(bateau):
        raise ValueError(
            f"setSegmentBateau: La valeur {bateau} n'est pas un bateau")
    elif not (0 <= numSeg < len(bateau[const.BATEAU_SEGMENTS])):
        raise ValueError(
            f"setSegmentBateau: La valeur est en dehors des limites")
    elif not type_segment(segmt):
        raise ValueError(
            f"setSegmentBateau: La valeur {bateau} n'est pas un bateau")
    getSegmentsBateau(bateau)[numSeg] = segmt
    return getSegmentsBateau(bateau)[numSeg]


def getCoordonneesBateau(bateau: dict) -> list:
    lst = []
    if not type_bateau(bateau):
        raise ValueError(
            f"getCoordonneesBateau: La valeur {bateau} n'est pas un bateau")
    for i in range(getTailleBateau(bateau)):
        lst.append(getCoordonneesSegment(bateau[const.BATEAU_SEGMENTS][i]))
    return lst


def peutPlacerBateau(bateau: dict, first_case: tuple, placement: bool) -> bool:
    if not type_bateau(bateau):
        raise ValueError(
            f"peutPlacerBateau: La valeur {bateau} n'est pas un bateau")
    elif not type_coordonnees(first_case) or first_case is None:
        raise ValueError(
            f"peutPlacerBateau : le paramètre {first_case} ne correspond pas à des coordonnées.")
    tailleBateau = getTailleBateau(bateau) - 1
    y, x = first_case
    if placement:
        # horizontale
        finBateau = (y, x + tailleBateau)
    else:
        # verticale
        finBateau = (y + tailleBateau, x)
    return type_coordonnees(finBateau)

def estPlaceBateau(bateau: dict) -> bool:
    if not type_bateau(bateau):
        raise ValueError(
            f"estPlaceBateau: La valeur {bateau} n'est pas un bateau")
    positionne = True
    i = 0
    while positionne and i < len(bateau.get(const.BATEAU_SEGMENTS)):
        if getCoordonneesBateau(bateau)[i] == None:
            positionne = False
        i += 1
    return positionne


def sontVoisinsBateau(bateau1: dict, bateau2: dict) -> bool:
    if not type_bateau(bateau1):
        raise ValueError(
            f"peutPlacerBateau: La valeur {bateau1} n'est pas un bateau")
    if not type_bateau(bateau2):
        raise ValueError(
            f"peutPlacerBateau: La valeur {bateau2} n'est pas un bateau")
    a = getSegmentsBateau(bateau1)
    b = getSegmentsBateau(bateau2)
    res = False
    i = 0
    while i < len(a) and not res:
        j = 0
        while j < len(b) and not res:
            if sontVoisins(getCoordonneesSegment(a[i]), getCoordonneesSegment(b[j])):
                res = True
            j += 1
        i += 1
    return res





