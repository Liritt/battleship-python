# model/Manuel.py
#
from view import window
from model.Joueur import getNomJoueur, type_joueur, construireJoueur

def placerBateauxManuel(joueur: dict) -> None:
    if not type_joueur(joueur):
        raise ValueError(f"reinitialiserBateauxJoueur: {joueur} n'est pas un joueur")
    window.afficher(joueur)
    window.display_message(f"{getNomJoueur(joueur)} : placez vos bateaux")
    window.placer_bateaux()







