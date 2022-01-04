# Joueur.py

from model.Bateau import type_bateau, construireBateau
from model.Grille import type_grille, construireGrille
from model.Constantes import *

#
# Un joueur est représenté par un dictionnaire contenant les couples (clé, valeur) suivants :
#  const.JOUEUR_NOM : Nom du joueur de type str
#  const.JOUEUR_LISTE_BATEAUX : Liste des bateaux du joueur
#  const.JOUEUR_GRILLE_TIRS : Grille des tirs sur les bateaux adverses
#  const.JOUEUR_GRILLE_ADVERSAIRE : une grille des tirs de l'adversaire pour tester la fonction de tir
#  de l'adversaire.
#


def type_joueur(joueur: dict) -> bool:
    """
    Retourne <code>True</code> si la liste semble correspondre à un joueur,
    <code>false</code> sinon.

    :param joueur: Dictionnaire représentant un joueur
    :return: <code>True</code> si le dictionnaire représente un joueur, <code>False</code> sinon.
    """
    return type(joueur) == dict and len(joueur) >= 4 and \
        len([p for p in [ const.JOUEUR_NOM, const.JOUEUR_LISTE_BATEAUX, const.JOUEUR_GRILLE_TIRS] if p not in joueur]) == 0 and \
        type(joueur[const.JOUEUR_NOM]) == str and type(joueur[const.JOUEUR_LISTE_BATEAUX]) == list \
        and type_grille(joueur[const.JOUEUR_GRILLE_TIRS]) \
        and all(type_bateau(v) for v in joueur[const.JOUEUR_LISTE_BATEAUX])


def construireJoueur(nomJoueur: str, nomsBateaux: list) -> dict:
    lst = []
    for i in range(len(nomsBateaux)):
        lst.append(construireBateau(nomsBateaux[i]))
    joueur = {
        const.JOUEUR_NOM: nomJoueur,
        const.JOUEUR_LISTE_BATEAUX: lst,
        const.JOUEUR_GRILLE_TIRS: construireGrille(),
        const.JOUEUR_GRILLE_ADVERSAIRE: construireGrille()
    }
    return joueur


def getNomJoueur(joueur: dict) -> str:
    if not type_joueur(joueur):
        raise ValueError(f"getNomJoueur: {joueur} n'est pas un joueur")
    else:
        nomJoueur = joueur.get(const.JOUEUR_NOM)
    return nomJoueur


def getNombreBateauxJoueur(joueur: dict) -> int:
    if not type_joueur(joueur):
        raise ValueError(f"getNombreBateauxJoueur: {joueur} n'est pas un joueur")
    else:
        nbBateauxJoueur = len(joueur.get(const.JOUEUR_LISTE_BATEAUX))
    return nbBateauxJoueur


def getBateauxJoueur(joueur: dict) -> list:
    if not type_joueur(joueur):
        raise ValueError(f"getBateauxJoueur: {joueur} n'est pas un joueur")
    else:
        lstBateauxJoueur = joueur.get(const.JOUEUR_LISTE_BATEAUX)
    return lstBateauxJoueur
