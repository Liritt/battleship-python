# Voici la liste des états possible pour l'IA
# 1. Aucun segment touché (data: None)
#   => elle tire aléatoirement dans la grille sans toucher de case voisine à un bateau déjà coulé
# 2. Un seul segment touché (data: coord)
#   => elle tire sur un nouveau coté de ce segment aléatoirement
# 3. Au moins deux segments touchés (data: coords, direction)
#   => elle tire à coté de ces segments dans la même direction
#       => si ce tire échoue, elle inverse la direction
#
# Quand l'IA coule un bateau, elle retourne à l'état n°1
#
# Directions : g: gauche, h: haut, d: droite, b: bas

from model.Bateau import getTailleBateau
from model.Coordonnees import type_coordonnees
from model.Grille import marquerCouleGrille
from model.Joueur import getBateauxJoueur, getGrilleTirsAdversaire, getGrilleTirsJoueur, getNomJoueur, placerBateauJoueur, type_joueur
from view import window
from random import randint, randrange, shuffle
from model.Constantes import *  

def placerBateauxIA(joueur: dict) -> None:
    """Demande à l'IA de placer ses bateaux

    Args:
        joueur (dict): Le joueur
    """
    if not type_joueur(joueur):
        raise ValueError(f'placerBateauxManuel : le paramètre {joueur} n’est pas de type Joueur')
    
    # Pour tous les bateaux à poser
    bateaux = getBateauxJoueur(joueur)
    for i in range(len(bateaux)):
        tailleBateau = getTailleBateau(bateaux[i])

        # Génère des coordonnées aléatoires dans la grille, et lorsque cela est possible, on place le bateau
        horizontale = bool(randint(0,1))
        reussi = False
        while not reussi:
            first_case = (randint(0, const.DIM), randint(0, const.DIM))
            reussi = type_coordonnees(first_case) and placerBateauJoueur(joueur, bateaux[i], first_case, horizontale)

    return None


def setIAEtat(joueur: dict, code: int, data: dict) -> None:
    """Modifie les données de l'IA dans le joueur

    Args:
        joueur (dict): Le joueur
        code (int): Le code de l'état (1, 2 ou 3)
        data (dict): Les donnees de l'état

    Returns:
        [type]: [description]
    """
    if not type_joueur(joueur):
        raise ValueError(f'setIAEtat : le paramètre {joueur} n’est pas de type Joueur')
    
    joueur['ia'] = {
        'code': code,
        'data': data
    }

    return None


def getIAEtat(joueur: dict) -> dict:
    """Récupère les données de l'IA dans le joueur

    Args:
        joueur (dict): Le joueur

    Returns:
        dict: Les données de l'IA
    """
    if not type_joueur(joueur):
        raise ValueError(f'getIAEtat : le paramètre {joueur} n’est pas de type Joueur')
    
    if 'ia' in joueur:
        etat = joueur['ia']
    else:
        etat = {
            'code': 1,
            'data' : {}
        }
    
    return etat


def getDirection(coord1: tuple, coord2: tuple) -> str:
    """Détermine la direction entre deux coordonnées
    (cette fonction ne prend pas en compte les diagonales)

    Args:
        coord1 (tuple): La première coordonnée
        coord2 (tuple): La deuxième coordonnée

    Returns:
        str: La direction (g ou h ou d ou b)
    """
    if coord1 == None or not type_coordonnees(coord1):
        raise ValueError(f'getDirection : le paramètre {coord1} n’est pas de type Coordonnée')
    if coord2 == None or not type_coordonnees(coord2):
        raise ValueError(f'getDirection : le paramètre {coord2} n’est pas de type Coordonnée')

    c1y, c1x = coord1
    c2y, c2x = coord2
    direction = None
    if c2x < c1x:
        direction = 'g'
    elif c2y < c1y:
        direction = 'h'
    elif c2x > c1x:
        direction = 'd'
    elif c2y > c1y:
        direction = 'b'
    
    return direction


def getProchaineCase(coord: tuple, direction: str) -> tuple:
    """Détermine la prochaine case selon la direction

    Args:
        coord (tuple): La coordonnée de la case initiale
        direction (str): La direction de la prochaine case

    Returns:
        tuple: La prochaine case
    """
    if coord == None or not type_coordonnees(coord):
        raise ValueError(f'getProchaineCase : le paramètre {coord} n’est pas de type Coordonnée')
    if direction not in ['g', 'h', 'd', 'b']:
        raise ValueError(f'getProchaineCase : le paramètre {direction} n’est pas de type direction')
    
    cy, cx = coord
    prochaineCase = None

    if direction == 'g':
        prochaineCase = (cy, cx-1)
    elif direction == 'h':
        prochaineCase = (cy-1, cx)
    elif direction == 'd':
        prochaineCase = (cy, cx+1)
    else:
        prochaineCase = (cy+1,cx)
    
    return prochaineCase


def getDirectionInverse(direction: str) -> str:
    """Détermine l'inverse de la direction

    Args:
        direction (str): La direction

    Returns:
        str: L'inverse de la direction
    """
    if direction not in ['g', 'h', 'd', 'b']:
        raise ValueError(f'getProchaineCase : le paramètre {direction} n’est pas de type direction')
    
    inverse = None
    
    if direction == 'g':
        inverse = 'd'
    elif direction == 'h':
        inverse = 'b'
    elif direction == 'd':
        inverse = 'g'
    else:
        inverse = 'h'
    
    return inverse


def peutChoisirCaseIACode1(grille: list, coord: tuple) -> bool:
    """Détermine si l'IA peut choisir la case dans l'état 1
    (si la case n'a pas déjà été choisie et si la case n'est pas voisine d'un bateau déjà coulé)

    Args:
        grille (list): La grille

    Returns:
        bool: True si l'IA peut choisir cette case, False sinon
    """
    cy, cx = coord

    cases_voisines = []
    # 
    #  x
    #
    cases_voisines.append((cy, cx))
    # 
    # xo
    #
    cases_voisines.append((cy, cx - 1))

    # x
    #  o
    #
    cases_voisines.append((cy - 1, cx - 1))

    #  x
    #  o
    #
    cases_voisines.append((cy - 1, cx))

    #   x
    #  o
    #
    cases_voisines.append((cy - 1, cx + 1))

    #   
    #  ox
    #
    cases_voisines.append((cy, cx + 1))

    #   
    #  o
    #   x
    cases_voisines.append((cy + 1, cx + 1))

    #   
    #  o
    #  x
    cases_voisines.append((cy + 1, cx))

    #   
    #  o
    # x
    cases_voisines.append((cy + 1, cx - 1))

    peutPlacer = True
    i = 0
    while peutPlacer and i < len(cases_voisines):
        if type_coordonnees(cases_voisines[i]) and grille[cases_voisines[i][0]][cases_voisines[i][1]] in [const.TOUCHE, const.COULE]:
            peutPlacer = False
        i += 1
    
    # Vérification de la case n'a pas déjà été choisie
    if grille[coord[0]][coord[1]] != None:
        peutPlacer = False

    return peutPlacer


def choisirCaseIACode1(joueur: dict) -> tuple:
    """Choisie la case à tirer dans l'état 1
    1. Aucun segment touché (data: None)
        => elle tire aléatoirement dans la grille sans toucher de case voisine à un bateau déjà coulé

    Args:
        joueur (dict): Le joueur

    Returns:
        tuple: La case choisie
    """
    reussi = False
    while not reussi:
        case = (randint(0, const.DIM-1), randint(0, const.DIM-1))
        if peutChoisirCaseIACode1(getGrilleTirsAdversaire(joueur), case):
            caseChoisie = case
            reussi = True
    
    return caseChoisie


def choisirCaseIACode2(joueur: dict) -> tuple:
    """Choisie la case à tirer dans l'état 2
    2. Un seul segment touché (data: coord)
        => elle tire sur un nouveau coté de ce segment aléatoirement

    Args:
        joueur (dict): Le joueur

    Returns:
        tuple: La case choisie
    """

    etat = getIAEtat(joueur)
    data = etat['data']
    segTouche = data['seg_touche']
    cy, cx = segTouche

    cases_possibles = []
    #   
    # xo
    #   
    cases_possibles.append((cy, cx - 1))

    #  x
    #  o
    #   
    cases_possibles.append((cy - 1, cx))

    #   
    #  ox
    #   
    cases_possibles.append((cy, cx + 1))

    #   
    #  o
    #  x
    cases_possibles.append((cy + 1, cx))

    shuffle(cases_possibles)

    # Choisie une case non essayé sur le coté du segment touché
    grille = getGrilleTirsAdversaire(joueur)
    caseChoisie = None
    i = 0
    while caseChoisie == None and i < len(cases_possibles):
        if type_coordonnees(cases_possibles[i]) and grille[cases_possibles[i][0]][cases_possibles[i][1]] == None:
            caseChoisie = cases_possibles[i]
        i += 1
    
    return caseChoisie
        

def choisirCaseIACode3(joueur: dict) -> tuple:
    """Choisie la case à tirer dans l'état 3
    3. Au moins deux segments touchés (data: coords, direction)
        => elle tire à coté de ces segments dans la même direction
            => si ce tire échoue, elle inverse la direction

    Args:
        joueur (dict): Le joueur

    Returns:
        tuple: La case choisie
    """
    etat = getIAEtat(joueur)
    data = etat['data']
    segsTouches = data['segs_touches']
    direction = data['direction']

    # récupère la case dans la direction voulu
    caseChoisie = None
    caseDirection1 = getProchaineCase(segsTouches[len(segsTouches)-1], direction)
    caseDirection2 = getProchaineCase(segsTouches[0], direction)
    if(getDirection(segsTouches[0], segsTouches[len(segsTouches)-1]) == direction):
        caseChoisie = caseDirection1
    else:
        caseChoisie = caseDirection2
    
    # Si la case n'est pas possible, on choisie la case de l'autre direction
    #if not peutChoisirCaseIACode1(getGrilleTirsAdversaire(joueur), caseChoisie):
    #    if caseChoisie == caseDirection1: caseChoisie = caseDirection2
    #    else: caseChoisie = caseDirection1
    
    return caseChoisie


def choisirCaseIA(joueur: dict) -> tuple:
    """Demande à l'IA de choisir une case à attaquer

    Args:
        joueur (dict): Le joueur

    Returns:
        tuple: La case choisie par l'IA
    """
    if not type_joueur(joueur):
        raise ValueError(f'choisirCaseIA : le paramètre {joueur} n’est pas de type Joueur')
    
    etat = getIAEtat(joueur)
    caseChoisie = None

    if etat['code'] == 1:
        caseChoisie = choisirCaseIACode1(joueur)
    elif etat['code'] == 2:
        caseChoisie = choisirCaseIACode2(joueur)
    elif etat['code'] == 3:
        caseChoisie = choisirCaseIACode3(joueur)
        

    
    return caseChoisie


def traiterResultatIA(joueur: dict, coord: tuple, reponse: str):
    """Traite le résultat du tir dans la grille du joueur

    Args:
        joueur (dict): Le joueur
        coord (tuple): Les coordonnées
        reponse (str): La réponse du tir
    """
    if not type_joueur(joueur):
        raise ValueError(f'traiterResultatIA : le paramètre {joueur} n’est pas de type Joueur')
    if not type_coordonnees(coord):
        raise ValueError(f'traiterResultatIA : le paramètre {coord} n’est pas de type Coordonnée')
    if reponse not in [const.RATE, const.TOUCHE, const.COULE]:
        raise ValueError(f'traiterResultatIA : le paramètre {reponse} n’est pas une réponse')
    
    grille = getGrilleTirsJoueur(joueur)
    if reponse == const.COULE:
        marquerCouleGrille(grille, coord)
    else:
        grille[coord[0]][coord[1]] = reponse
    
    # On enregistre le nouvel état de l'IA
    etat = getIAEtat(joueur)
    if reponse == const.COULE:
        # Si l'IA vient de couler un bateau, on la fait repasser à l'état 1
        setIAEtat(joueur, 1, {})
    elif etat['code'] == 1 and reponse == const.TOUCHE:
        # Si l'IA vient de toucher pour la première fois un segment, on la fait passer à l'état 2
        setIAEtat(joueur, 2, {'seg_touche': coord})
    elif etat['code'] == 2 and reponse == const.TOUCHE:
        # Si l'IA vient de toucher un deuxième segment, on la fait passer à l'état 3
        segsTouches = []
        segsTouches.append(etat['data']['seg_touche'])
        segsTouches.append(coord)
        setIAEtat(joueur, 3, {'segs_touches': segsTouches, 'direction': getDirection(segsTouches[0], coord)})
    elif etat['code'] == 3 and reponse == const.TOUCHE:
        # Si l'IA vient de toucher un nème segment à l'état 3, on continue
        segsTouches = etat['data']['segs_touches']
        segsTouches.append(coord)
        direction = etat['data']['direction']
        setIAEtat(joueur, 3, {'segs_touches': segsTouches, 'direction': direction})
    elif etat['code'] == 3 and reponse == const.RATE:
        # Si l'IA vient de rate à l'état 3, on inverse la direction
        anciensSegTouche = etat['data']['segs_touches']
        direction = getDirectionInverse(etat['data']['direction'])
        setIAEtat(joueur, 3, {'segs_touches': anciensSegTouche, 'direction': direction})
    
    return None


def construireActeurIA(joueur: dict) -> dict:
    """Crée un acteur

    Args:
        joueur (dict): Le joueur

    Returns:
        dict: L'acteur
    """
    if not type_joueur(joueur):
        raise ValueError(f'construireActeurIA : le paramètre {joueur} n’est pas de type Joueur')

    acteur = {
        const.ACTEUR: joueur,
        const.ACTEUR_PLACER_BATEAUX: placerBateauxIA,
        const.ACTEUR_CHOISIR_CASE: choisirCaseIA,
        const.ACTEUR_TRAITER_RESULTAT: traiterResultatIA
    }

    return acteur
