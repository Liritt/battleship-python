# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from model.Jeu import getListeBateaux, jouerJeu

from model.Manuel import construireActeurManuel, placerBateauxManuel, choisirCaseTirManuel, traiterResultatTirManuel
from model.Constantes import *
from model.Joueur import construireJoueur, repondreTirJoueur
from view import window

def main_test():
 joueur1 = construireJoueur("Galérien", getListeBateaux())
 joueur2 = construireJoueur("Hamdoulila", getListeBateaux())
 jouerJeu(joueur1, joueur2)
 construireActeurManuel(joueur1)
 construireActeurManuel(joueur2)
 placerBateau = joueur1.get(const.ACTEUR_PLACER_BATEAUX)
 choisir_case = joueur1.get(const.ACTEUR_CHOISIR_CASE)
 traiterResultat = joueur1.get(const.ACTEUR_TRAITER_RESULTAT)
 placerBateau(joueur1)
 choisir_case(joueur1)
 traiterResultat(joueur1, choisir_case(joueur1), repondreTirJoueur(joueur1, choisir_case(joueur1)))
 placerBateau(joueur2)
 choisir_case(joueur2)
 traiterResultat(joueur2, choisir_case(joueur2), repondreTirJoueur(joueur2, choisir_case(joueur2)))

if __name__ == '__main__' :
 main_test()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
