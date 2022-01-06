# model/Manuel.py
#
from view import window
from model.Joueur import getGrilleTirsAdversaire, getGrilleTirsJoueur, getNomJoueur, repondreTirJoueur, type_joueur, construireJoueur, marquerCouleGrille
from model.Coordonnees import type_coordonnees
from model.Constantes import *


def placerBateauxManuel(joueur: dict) -> None:
    if not type_joueur(joueur):
        raise ValueError(
            f"reinitialiserBateauxJoueur: {joueur} n'est pas un joueur")
    window.afficher(joueur)
    window.display_message(f"{getNomJoueur(joueur)} : placez vos bateaux")
    window.placer_bateaux()


def choisirCaseTirManuel(joueur: dict) -> tuple:
    if not type_joueur(joueur):
        raise ValueError(
            f"reinitialiserBateauxJoueur: {joueur} n'est pas un joueur")
    window.afficher(joueur)
    window.display_message(
        f"{getNomJoueur(joueur)} : choisissez la case où vous voulez tirer")
    window.set_action("Choisissez la case de tir")
    return window.get_clicked_cell(2)[0]


def traiterResultatTirManuel(joueur: dict, coord: tuple, reponse: str) -> None:
    if not type_joueur(joueur):
        raise ValueError(
            f"traiterResultatTirManuel: {joueur} n'est pas un joueur")
    if not type_coordonnees(coord):
        raise ValueError(
            f"traiterResultatTirManuel: les valeurs {coord} ne correspondent pas à des coordonnées")
    if repondreTirJoueur(joueur, coord) == const.RATE:
        getGrilleTirsJoueur(joueur)[coord[0]][coord[1]] = const.RATE
    if repondreTirJoueur(joueur, coord) == const.TOUCHE:
        getGrilleTirsJoueur(joueur)[coord[0]][coord[1]] = const.TOUCHE
    if repondreTirJoueur(joueur, coord) == const.COULE:
        marquerCouleGrille(getGrilleTirsJoueur(joueur), coord)