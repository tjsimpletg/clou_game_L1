from clou import *

# Ce fichier contient les fonctions permettant de tester les fonctions dans le fichier "Clou.py"
#


# Fonction lançant l'ensemble des fonctions de tests implantées dans la suite du fichier
#
def run_tests():
    #1. tester les saisis
    print('====>test les saisis commence:') 
    test_est_dans_les_trois_partie()
    test_est_dans_les_trois_modeles()
    test_est_dans_grille()
    print('tous les tests des saisis OK !')
    print(v)
    print(v)
    

    
    #2. tests verifient la validité des deplacement
    print('====>test pour verifier la validité des deplacements commence:')
    test_contenu_noncaptu()
    test_distance_noncaptu()
    test_contenu_captu()
    test_distance_captu()
    test_direction()
    print('tous les tests pour verifier la validité des deplacemen  OK !' )
    print(v)
    print(v)
    #3. tests depacement
    print('====>test depacement commence: ')
    test_depacement_simple()
    test_deplacement_capture()
    test_effet_pion_et_afficher()
    print('les deux types de deplacement OK !')
    print(v)
    print(v)

    #4. tests les fonctions de IA automatiquement
    print('====>commence à tester les fonctions de IA AUTOMATIQUEMENT:')
    test_recuperer_les_pions_de_j1_non_bloque()
    test_recuperer_les_pions_de_j2_non_bloque()
    test_les_cords_de_pion_depart_aleatoire()
    test_les_cords_de_deplacement_aleatoire()
    print('tous les tests des fonctions de IA  OK !')
    print(v)
    print(v)
    
    #5. test fin partie
    print('====>test fin partie commence:')
    test_fin_partie()
    print(v)
    print('          TOUS les tests  OK ! ')
    
    


#
#   Les fonctions de tests
#


# Test de la fonction est_dans_grille()
def test_est_dans_grille():
    '''test de assertation du jeu sur les coordonnees'''
    print(v)
    print('==>test cordonnees saisis,sous forme comme A1,A2')
    cord = saisir_coordonnees()
    assert est_dans_grille(cord)==True,'erreur,les coordonnees que vous saisiez ne sont pas dans grille'
    print('test_est_dans_grille OK !')
    print(v)

    
    
# Test si il est dans les trois partie
def test_est_dans_les_trois_partie():
    print(v)
    print('==>saisir la numéro de partie et test si il est 1,2 ou 3')
    partie = input()
    assert partie in ('1','2','3'),'erreur,vous avez mal choisi la partie en commence.'
    print('test_est_dans_les_trois_partie OK !')
    print(v)

def test_est_dans_les_trois_modeles():
    '''Test si il est dans les trois modeles'''
    print(v)
    print("==>test saisir la modele de jeu. si il est 1,2 ou 3 ")
    modele = input()
    assert modele in ('1','2','3') , 'erreur, vous avez mal saisi la modele en commence !! '
    print('test_est_dans_les_deux_modeles OK !')
    print(v)

# Test de la fonction verifier_contenu_noncaptu(depart,arrive)
def test_contenu_noncaptu():
    print('==>test le contenu pour deplacement simple')
    afficher_grille(grille)
    depart = saisir_coordonnees()
    arrive = saisir_coordonnees()
    assert verifier_contenu_noncaptu(depart,arrive) == True,\
           'erreur,vous avez mal choisi contenu depart ou arrivée pour depacement_simple  !!'
    print('test_contenu_noncaptu OK !')
    print(v)


    
# Test de la fonction verifier_distance_noncaptu()
def test_distance_noncaptu():
    print(v)
    print('==>test la distance entre deux cases pour deplacement simple')
    afficher_grille(grille)
    depart = saisir_coordonnees()
    arrive = saisir_coordonnees()
    assert verifier_distance_noncaptu(depart,arrive) == True,'erreur, mal distance choisi pour deplacement simple !!'
    print('test_distance_noncaptu OK !')
    print(v)


# Test de la fonction verifier_contenu_captu()   
def test_contenu_captu():
    print(v)
    print('==>test le contenu pour deplacement capture')
    afficher_grille(grille)
    depart = saisir_coordonnees()
    arrive = saisir_coordonnees()
    assert verifier_contenu_captu(depart,arrive) == True ,\
           'erreur, mal choisi le pion pour captuer !!'
    print('test_contenu_captu OK !' )
    print(v)


    
# Test de la fonction verifier_distance_captu()
def test_distance_captu():
    print(v)
    print('==>test la distance entre deux cases pour deplacement capture')
    afficher_grille(grille)
    depart = saisir_coordonnees()
    arrive = saisir_coordonnees()
    assert verifier_distance_captu(depart,arrive) == True ,'erreur, mal distance choisi pour deplacement capture !!'
    print('test_distance_captu OK !')
    print(v)
    

    
# Test de la fonction verifier_direction()
def test_direction():
    print(v)
    print('==>test la direction entre deux cases')
    afficher_grille(grille)
    depart = saisir_coordonnees()
    arrive = saisir_coordonnees()
    assert verifier_direction(depart,arrive) == True,' erreur, mal choisi la direction !!'
    print('test_direction OK !')
    print(v)

    

#Test de la fonction deplacement_simple()  
def test_depacement_simple():
    print('==>saisiez une possibilité de depacement simple')
    afficher_grille(grille)
    depart = saisir_coordonnees()
    arrive = saisir_coordonnees()
    assert verifier_contenu_noncaptu(depart,arrive)  == True \
           and verifier_direction(depart,arrive) == True and verifier_distance_noncaptu(depart,arrive) == True,\
           'erreur,vous avez mal choisi la case depart ou arrivée pour depacement simple !!'
    print('test_depacement_simple OK !')
    print(v)
    



# Test de la fonctin deplacement_capture()
def test_deplacement_capture():
    print(v)
    print("==>test si il peut capturer un autre pion. saisiez une possibilité d'après la règle. ")
    afficher_grille(grille)
    depart = saisir_coordonnees()
    arrive = saisir_coordonnees()
    assert verifier_contenu_captu(depart,arrive) == True \
           and verifier_direction(depart,arrive) == True and verifier_distance_captu(depart,arrive) == True and \
           (verifier_captu_j1(depart,arrive) == True or verifier_captu_j2(depart,arrive) == True), \
           'erreur,vous avez mal choisi la case depart ou arrivée pour depacement capture !!'
    print('test_deplacement_capture OK !')
    print(v)

# Test effet après déplacement
def test_effet_pion_et_afficher():
    print('==>test si il change les pions que vous avez saisi' )
    afficher_grille(grille)
    print('saisiez cords depart:')
    depart = saisir_coordonnees()
    print('saisiez cords arrivé:')
    arrive = saisir_coordonnees()
    image_depart_init = image_cord(depart)
    image_arrive_init = image_cord(arrive)
    effet_pion_sans_afficher(depart,arrive)
    image_depart_apres = image_cord(depart)
    image_arrive_apres = image_cord(arrive)
    afficher_grille(grille)
    assert image_depart_init == image_arrive_apres and image_arrive_init == image_depart_apres ,"les pion n'est pas changés corrctement !!"
    effet_pion_sans_afficher(depart,arrive)
    print('effet_pion_sans_afficher OK !')
    print(v)


# Tests les fonctions de IA automatiquement
def test_recuperer_les_pions_de_j1_non_bloque():
    print(v)
    print('==>test si les pions de joueur 1 non bloqués récuperés par IA sont corrects.')
    print(v)
    liste_cords_non_bloquer = les_pions_de_j1_non_bloque()
    print(liste_cords_non_bloquer)
    liste_cords_non_bloquer_test = []
    liste_distinct = []
    for cord in liste_cords_non_bloquer:
                for ls in tous_lignes:
                        for cs in tous_colonnes2:
                                case = ls+cs
                                if deplacement_simple(cord,case) == True \
                                       or deplacement_captu_j1(cord,case) == True:
                                    liste_cords_non_bloquer_test.append(cord)
    for e in liste_cords_non_bloquer_test:
        if e not in liste_distinct :
            liste_distinct.append(e)
    print(liste_distinct)
    assert liste_cords_non_bloquer == liste_distinct ,'erreur, les pions non bloqués que IA récupère ne sont pas corrects !!' 
    print('test_recuperer_les_pions_de_j1_non_bloque() OK !' )
    print(v)


def test_recuperer_les_pions_de_j2_non_bloque():
    print(v)
    print('==>test si les pions de joueur 2 non bloqués récuperés par IA sont corrects.')
    print(v)
    liste_cords_non_bloquer = les_pions_de_j2_non_bloque()
    print(liste_cords_non_bloquer)
    liste_cords_non_bloquer_test = []
    liste_distinct = []
    for cord in liste_cords_non_bloquer:
                for ls in tous_lignes:
                        for cs in tous_colonnes2:
                                case = ls+cs
                                if deplacement_simple(cord,case) == True \
                                       or deplacement_captu_j2(cord,case) == True:
                                    liste_cords_non_bloquer_test.append(cord)
    for e in liste_cords_non_bloquer_test:
        if e not in liste_distinct :
            liste_distinct.append(e)
    print(liste_distinct)
    assert liste_cords_non_bloquer == liste_distinct,'erreur, les pions non bloqués que IA récupère ne sont pas corrects !!'
    print('test_recuerer_les_pions_de_j2_non_bloque() OK !')
    


def test_les_cords_de_pion_depart_aleatoire():
    print(v)
    print('==>test si le pion que IA choisi est dans les pions non bloqués récuperés par IA .')
    print(v)
    cord_depart = les_cords_de_pion_depart_aleatoire()
    liste_cords_non_bloquer = les_pions_de_j2_non_bloque()
    assert cord_depart in liste_cords_non_bloquer ,"erreur,le pion que IA choisi n'est pas dans les pions non bloqués récuperés par IA !!"
    print('test_les_cords_de_pion_depart_aleatoire OK !')
    print(v)


def test_les_cords_de_deplacement_aleatoire():
    print(v)
    print('==>test si le pion que IA choisi peut deplacer vers une autre case aleatoire .')
    print(v)
    cords_aleatoire = les_cords_de_deplacement_aleatoire()
    assert deplacement_simple(cords_aleatoire[0],cords_aleatoire[1]) == True \
           or deplacement_captu_j2(cords_aleatoire[0],cords_aleatoire[1]) == True,\
           "erreur, le pion que IA choisi ne peut pas déplacer !!"
    effet_pion(cords_aleatoire[0],cords_aleatoire[1])
    effet_pion_sans_afficher(cords_aleatoire[0],cords_aleatoire[1])
    print('test_les_cords_de_deplacement_aleatoire OK !')
    print(v)



# Test de la fonction fin_partie()
def test_fin_partie():
    print("==>test pour verifier si le jeu est fini ")
    pion_reste_j2 = 2
    afficher_grille(grille)
    print('vous peuvez marcher une fois dans ce test. esseyez de mettre pion noire gagner le jeu par une etape.')
    depart = cord_depart()
    arrive = cord_arrive()
    if deplacement_captu_j1(depart,arrive) == True:
        pion_reste_j2 -=1
    effet_pion(depart,arrive) # vous peuvez marcher une fois dans ce test. si vous avez choisi grille millieu comme test, esseyez de mettre pion noire gagner par une etape.
    assert pion_reste_j2 <= 1 ,"erreur, le jeu n'est pas fini !!"
    print("le jeu est bien fini   joueur1: •  win !!!  test_fin_partie OK !")
    
#
# Exécution des tests
#
#
run_tests()






