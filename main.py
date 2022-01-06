# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from model.Jeu import getListeBateaux, jouerJeu

from model.Manuel import placerBateauxManuel, choisirCaseTirManuel, traiterResultatTirManuel
from model.Constantes import *
from model.Joueur import construireJoueur, repondreTirJoueur
from view import window

def main_test():
 joueur1 = construireJoueur("Galérien", getListeBateaux())
 joueur2 = construireJoueur("Hamdoulila", getListeBateaux())
 jouerJeu(joueur1, joueur2)

if __name__ == '__main__' :
 main_test()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
