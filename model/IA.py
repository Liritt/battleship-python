from model.Coordonnees import type_coordonnees, sontVoisins
from model.Segment import construireSegment, getCoordonneesSegment, setEtatSegment, type_segment, setCoordonneesSegment, getEtatSegment, type_etat_segment
from model.Constantes import *
from model.Bateau import *
from model.Joueur import *
from model.Jeu import type_acteur
from random import randint
from view import window

const.IA_NOM = "Ordinateur"
const.IA_LISTE_BATEAUX = "Liste des bateaux"
const.IA_GRILLE_TIRS = "Grille des tirs"
const.IA_GRILLE_ADVERSAIRE = "Grille des tirs de l'adversaire"

def placerBateauIA(bateau: dict, first_case: tuple, horizontal: bool) -> None:
    if not type_bateau(bateau):
        raise ValueError(
            f"placerBateau: La valeur {bateau} n'est pas un bateau")
    elif not type_coordonnees(first_case) or first_case is None:
        raise ValueError(
            f"placerBateau: le paramètre {first_case} ne correspond pas à des coordonnées.")
    first_case = (randint(0, const.DIM), randint(0, const.DIM))
    caseDejaChoisis = []
    while first_case in caseDejaChoisis:
        first_case = (randint(0, const.DIM), randint(0, const.DIM))
        if first_case not in caseDejaChoisis:
            caseDejaChoisis.append(first_case)
    taille = getTailleBateau(bateau)
    for i in range(taille):
        segment = getSegmentBateau(bateau, i)
        if horizontal:
            setCoordonneesSegment(segment, (first_case[0], first_case[1] + i))
        else:
            setCoordonneesSegment(segment, (first_case[0] + i, first_case[1]))
    if not peutPlacerBateau(bateau, first_case, horizontal):
        raise RuntimeError(f"placerBateau: Le bateau dépasse de la grille")

def choisirCaseIA(joueur: dict) -> tuple:
    if not type_joueur(joueur):
        raise ValueError(
            f"reinitialiserBateauxJoueur: {joueur} n'est pas un joueur")
    caseDejaChoisis = []
    case_choisi = (randint(0, const.DIM), randint(0, const.DIM))
    while case_choisi in caseDejaChoisis:
        case_choisi = (randint(0, const.DIM), randint(0, const.DIM))
        if case_choisi not in caseDejaChoisis:
            caseDejaChoisis.append(case_choisi)
    return window.get_clicked_cell(2)[0]

def traiterResultatIA(joueur: dict, coord: tuple, reponse: str) -> None:
    if not type_joueur(joueur):
        raise ValueError(
            f"traiterResultatTirManuel: {joueur} n'est pas un joueur")
    if not type_coordonnees(coord):
        raise ValueError(
            f"traiterResultatTirManuel: les valeurs {coord} ne correspondent pas à des coordonnées")
    grille = getGrilleTirsJoueur(joueur)
    grille[coord[0]][coord[1]] = reponse
    if reponse == const.COULE:
        marquerCouleGrille(grille, coord)

def construireActeurIA(IA: dict) -> dict:
    if not type_acteur(IA):
        raise ValueError(f"Non, ce n'est pas possible de créer un bot avec {IA}, un peu de sérieux bon sang")
    IA = {
        const.IA_NOM: "Ordinateur",
        const.IA_LISTE_BATEAUX: placerBateauIA,
        const.IA_GRILLE_TIRS: choisirCaseIA,
        const.IA_GRILLE_TIRS_ADVERSAIRE: traiterResultatIA
    }