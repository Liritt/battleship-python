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


def jouerJeu(acteur1: dict, acteur2: dict) -> None:
    if not type_acteur(acteur1):
        raise ValueError(f"repondreTirJoueur: {acteur1} n'est pas un joueur")
    if not type_acteur(acteur2):
        raise ValueError(f"repondreTirJoueur: {acteur2} n'est pas un joueur")
    acteur1[const.ACTEUR_PLACER_BATEAUX](acteur1[const.ACTEUR])
    acteur2[const.ACTEUR_PLACER_BATEAUX](acteur2[const.ACTEUR])
    choix = randint(1, 2)
    if choix == 1:
        premierJoueur = acteur1
        adversaire = acteur2
    else:
        premierJoueur = acteur2
        adversaire = acteur1
    while (not estPerdantJoueur(acteur1[const.ACTEUR])) and not (estPerdantJoueur(acteur2[const.ACTEUR])):
        window.afficher(premierJoueur[const.ACTEUR])
        window.display_message(f"C'est au tour de {getNomJoueur(premierJoueur[const.ACTEUR])}")
        case_choisit = premierJoueur[const.ACTEUR_CHOISIR_CASE](premierJoueur[const.ACTEUR])
        resultat_tir = repondreTirJoueur(adversaire[const.ACTEUR], case_choisit)
        premierJoueur[const.ACTEUR_TRAITER_RESULTAT](premierJoueur[const.ACTEUR], case_choisit, resultat_tir)
        window.refresh()
        window.display_message(f"Tir en {case_choisit} : {resultat_tir}")
        clt = premierJoueur
        premierJoueur = adversaire
        adversaire = clt
    if estPerdantJoueur(acteur1):
        window.display_message( f"Le gagnant est {getNomJoueur(acteur2[const.ACTEUR])}" )
    if estPerdantJoueur(acteur2):
        window.display_message( f"Le gagnant est {getNomJoueur(acteur1[const.ACTEUR])}" )


def getListeBateaux() -> list:
    return [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.CROISEUR, const.TORPILLEUR]

