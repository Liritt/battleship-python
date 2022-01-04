# model/Segment.py

from model.Coordonnees import type_coordonnees
from model.Etat import type_etat_segment
from model.Constantes import *

#
# définit un segment de bateau :
# Un segment de bateau est un dictionnaire contenant les couples (clé, valeur) suivants :
#   - const.SEGMENT_COORDONNEES : Les coordonnées du segment sur la grille
#   - ccnst.SEGMENT_ETAT : L'état du segment (const.RATE ou const.TOUCHE)
#


def type_segment(objet: dict) -> bool:
    """
    Détermine si l'objet passé en paramètre peut être interprété ou non
    comme un segment de bateau.

    :param objet: Objet à analyser
    :return: True si l'objet peut correspondre à un segment
    False sinon.
    """
    return type(objet) == dict and \
        all([k in objet for k in [const.SEGMENT_COORDONNEES, const.SEGMENT_ETAT]]) \
        and type_coordonnees(objet[const.SEGMENT_COORDONNEES]) \
        and type_etat_segment(objet[const.SEGMENT_ETAT])


def construireSegment(coord: tuple = None) -> dict:
    # Construit un segment et le retourne
    if not type_coordonnees(coord):
        raise ValueError(
            f"construireSegment : le paramètre {coord} ne correspond pas à des coordonnées.")
    else:
        segment = {const.SEGMENT_COORDONNEES: coord,
                   const.SEGMENT_ETAT: const.INTACT}
    return segment


def getCoordonneesSegment(segment: dict) -> tuple:
    if not type_segment(segment):
        raise ValueError(
            f"getCoordonneesSegment : le paramètre {segment} n’est pas de type Segment.")
    else:
        coord = segment.get(const.SEGMENT_COORDONNEES)
    return coord


def getEtatSegment(segment: dict) -> str:
    if not type_segment(segment):
        raise ValueError(
            f"getCoordonneesSegment : le paramètre {segment} n’est pas de type Segment.")
    else:
        etat = segment.get(const.SEGMENT_ETAT)
    return etat


def setCoordonneesSegment(segment: dict, coord: tuple) -> None:
    if not type_coordonnees(coord):
        raise ValueError(
            f"setCoordonneesSegment : le paramètre {coord} ne correspond pas à des coordonnées.")
    elif not type_segment(segment):
        raise ValueError(
            f"setCoordonneesSegment : le paramètre {segment} n’est pas de type Segment.")
    else:
        segment.update({const.SEGMENT_COORDONNEES: coord})


def setEtatSegment(segment: dict, etat: str) -> None:
    if not type_etat_segment(etat):
        raise ValueError(
            f"setEtatSegment : le paramètre {etat} ne correspond pas à des coordonnées.")
    elif not type_segment(segment):
        raise ValueError(
            f"setEtatSegment : le paramètre {segment} n’est pas de type Segment.")
    else:
        segment.update({const.SEGMENT_ETAT: etat})
