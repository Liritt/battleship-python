# model/Jeu.py

#
#  Module mettant en place les joueurs
#
from model.Bateau import placerBateau
from model.Joueur import estPerdantJoueur, getBateauxJoueur, placerBateauJoueur, type_joueur, getNomJoueur
from model.Constantes import *
from random import randint
from view import window
from model.Manuel import choisirCaseTirManuel, repondreTirJoueur, traiterResultatTirManuel, placerBateauxManuel

# Pour jouer, un joueur doit être capable de :
# - placer ses bateaux
# - choisir une case pour tirer
# - traiter le résultat d'un tir
# Pour cela, on crée un acteur : dictionnaire
#       const.ACTEUR : Joueur (voir construireJoueur)
#       const.ACTEUR_PLACER_BATEAUX : fonction permettant de placer les bateaux
#       const.ACTEUR_CHOISIR_CASE : fonction permettant de choisir la case où le tir aura lieu
#       const.ACTEUR_TRAITER_RESULTAT : fonction permettant de traiter le résultat d'un précédent tir

def type_acteur(agent: dict) -> bool:
    """
    Détermine si le tuple passé en paramètre peut être un agent ou non
    :param agent: Agent à tester
    :return: True si c'est un agent, False sinon
    """
    return type(agent) == dict and \
        all(k in agent for k in [const.ACTEUR,
                                 const.ACTEUR_PLACER_BATEAUX,
                                 const.ACTEUR_CHOISIR_CASE,
                                 const.ACTEUR_TRAITER_RESULTAT]) and \
        type_joueur(agent[const.ACTEUR]) and \
        callable(agent[const.ACTEUR_PLACER_BATEAUX]) and callable(agent[const.ACTEUR_CHOISIR_CASE]) and \
        callable(agent[const.ACTEUR_TRAITER_RESULTAT])


def jouerJeu(joueur1: dict, joueur2: dict) -> None:
    if not type_joueur(joueur1):
        raise ValueError(f"repondreTirJoueur: {joueur1} n'est pas un joueur")
    if not type_joueur(joueur2):
        raise ValueError(f"repondreTirJoueur: {joueur2} n'est pas un joueur")
    placerBateauxManuel(joueur1)
    placerBateauxManuel(joueur2)
    choix = randint(1, 2)
    if choix == 1:
        premierJoueur = joueur1
        deuxiemeJoueur = joueur2
    else:
        premierJoueur = joueur2
        deuxiemeJoueur = joueur1
    while not estPerdantJoueur(joueur1) and not estPerdantJoueur(joueur2):
        window.afficher(premierJoueur)
        window.display_message(f"C'est au tour de {getNomJoueur(premierJoueur)}")
        case_choisit = choisirCaseTirManuel(premierJoueur)
        resultat_tir = repondreTirJoueur(deuxiemeJoueur, case_choisit)
        traiterResultatTirManuel(premierJoueur, case_choisit, resultat_tir)
        window.refresh()
        window.display_message(f"Tir en coordonnees_case : {case_choisit}")
        clt = premierJoueur
        premierJoueur = deuxiemeJoueur
        deuxiemeJoueur = clt
    if estPerdantJoueur(joueur1):
        window.display_message( f"Le gagnant est {getNomJoueur(joueur1)}" )
    if estPerdantJoueur(joueur2):
        window.display_message( f"Le gagnant est {getNomJoueur(joueur2)}" )


def getListeBateaux() -> list:
    return [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.CROISEUR, const.TORPILLEUR]

