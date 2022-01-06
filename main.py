# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from model.Bateau import contientSegmentBateau
from model.Jeu import getListeBateaux, jouerJeu

from model.Manuel import construireActeurManuel, placerBateauxManuel, choisirCaseTirManuel, traiterResultatTirManuel
from model.Constantes import *
from model.Joueur import construireJoueur, repondreTirJoueur
from view import window

def main_test():
 acteur1 = construireActeurManuel(construireJoueur("Galérien", getListeBateaux()))
 acteur2 = construireActeurManuel(construireJoueur("Hamdoulila", getListeBateaux()))
 jouerJeu(acteur1, acteur2)

if __name__ == '__main__' :
 main_test()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
