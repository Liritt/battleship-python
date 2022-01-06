# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

from model.Manuel import placerBateauxManuel, choisirCaseTirManuel
from model.Constantes import *
from model.Joueur import construireJoueur, repondreTirJoueur
from view import window

def main_test():
 j = construireJoueur("Galérien", [const.PORTE_AVION, const.CUIRASSE,
 const.CROISEUR, const.TORPILLEUR])
 placerBateauxManuel(j)
 for i in range(4):
    case_choisit = choisirCaseTirManuel(j)
    print(case_choisit)
    resultat_tir = repondreTirJoueur(j,  case_choisit)
    window.refresh()
 window.set_action("Pour terminer, cliquez dans la grille de DROITE")
 window.get_clicked_cell(2)

if __name__ == '__main__' :
 main_test()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
