# -*- coding: utf-8 -*- 2
import sys
import random
random.seed()

#### REPRESENTATION DES DONNEES

###initialisation des grilles et autres variables de jeu
symbole=['|','•','o','_______________','‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾','',' ']
    # les symboles pour faire les dessins des grilles


#### Les extraits de la liste symbole


m=symbole[0]
# m est <symbole millieu tirer>
b=symbole[1]
# b est <pion black>
w=symbole[2]
# w est <pion white>
h=symbole[3]
# h est <symbole ligne en haut>
ba=symbole[4]
# ba est <symbole ligne en bas>
v=symbole[5]
# v est <symbole un vide>
dv=symbole[6]
# dv est <symbole double vides>

nombre_de_coups_j1 = 0
nombre_de_coups_j2 = 0
#initialisation du nombre de coups déjà joué

tous_lignes=['A','B','C','D']
tous_colonnes2 = ['1','2','3','4']
tous = [0,1,2,3]

# La domaine de definition des coordonnees

grille_debut=[[b,b,b,b],\
              [b,b,b,b],\
              [w,w,w,w],\
              [w,w,w,w]]


grille_millieu = [[b,w,dv,dv],\
                  [w,w,b,dv],\
                  [w,b,dv,dv],\
                  [w,b,b,dv]]


grille_fin = [[b,b,w,dv],\
              [dv,dv,dv,w],\
              [dv,dv,dv,b],\
              [dv,dv,dv,b]]


joueur_courant = 1

# On met une liste de liste pour la sturture de donnees





####### FONCTIONS


### REPRESENTATION GRAPHIQUE

def bienvenu():
        print(v),
        print(v),
        print(v),
        print( "              ☞  Bienvune à mon jeu CLOU ~    "),
        print(v)

# Je vous dis Bienvenu.


def afficher_grille(grille_):
        '''Pour afficher la grille variable pendant tout le jeu.'''
        print(v),
        print(v),
        print(v,v,v,v,v,1,v,v,2,v,v,3,v,v,4),
        print(v,v,v,v,h),
        for l in tous:
                print(v,tous_lignes[l],m,end = ' ') # on utilse deux boucles pour la affichage.
                for c in tous:
                        print(grille_[l][c],m,end = ' ')
                print('\n',v,v,v,ba)
        print(dv,dv,dv,dv)

 
def afficher_grille_init():
        '''Pour afficher les trois parties de jeu et à vous choisiez un commencer le jeu'''
        afficher_grille(grille_debut),
        print(dv,dv,v,"grille_debut"),
        afficher_grille(grille_millieu),
        print(dv,dv,"grille_millieu"),
        afficher_grille(grille_fin),
        print(dv,dv,dv,"grille_fin"),
        print(v),
        print(dv,' joueur 1:  • ',dv,dv,'joueur 2:  o '),
        print(v),
        print('*les cordonnees sont sous forme comme A1,A2.'),
        print(v)




#
### fonctions des saisies
#
#

def saisir_coordonnees():
        '''pour saisir cordonnees en type 'str' '''
        cords=input("====> ")
        if len(cords) == 2:
                if est_dans_grille(cords) == False:
                        print("les coordonnees que vous avez saisi ne sont pas dans grille !! resaisez le:")
                        return saisir_coordonnees()
                return cords
        print("le formet des cordonnées que vous avez saisi sont pas correct !! resaisiez le : ")
        return saisir_coordonnees()



def est_dans_grille(cord) :
        '''verifier si les cordonnees sont dans grille'''
        if (cord[0] in tous_lignes) and (cord[1] in tous_colonnes2):
                return True
        return False


def saisi_periode():
        '''pour choisir la partie à commencer'''
        print(v)
        print('*choisiez une grille parmi les trois pour commencer à jouer un tour de jeu')
        periode = input('''commencez le jeu par partie debut tapez 1, 
commencez le jeu par partie millieu tapez 2,
commencez le jeu par partie fin tapez 3,
========>''')
        if  periode in ('1','2','3'):
                return periode
        else:
                print('vous avez mal saisi !! resaisiez le ! ')
                return saisi_periode()


def saisi_jeu_modele():
        '''choisir la modèle de jeu, joueur contre joueur ou joueur contre IA'''
        modele = input('''commencez le jeu en modèle joueur contre joueur tapez 1,
commencez le jeu en modèle joueur contre IA naïve tapez 2,
commencez le jeu en modèle joueur contre IA avancé tapez 3
========>''')
        if modele in ('1','2','3'):
                return modele
        else:
                print('vous avez mal saisi !! resaisiez le ! ')
                return saisi_jeu_modele()



#
## antre fonctions
#

def choisi_periode_en_commence():
        '''return la grille que vous choisiez'''
        if periode == '1':
                print(v)
                print(' *le jeu est commencé aleatoirement par j1 ou j2.')
                return grille_debut
        if periode == '2':
                print(v)
                print(' *le jeu est commencé aleatoirement par j1 ou j2.')
                return grille_millieu
        if periode == '3':
                print(v)
                print(' *le jeu est commencé aleatoirement par j1 ou j2.')
                return grille_fin


    
def pion_reste_j1():
        '''indiquer nombre de pion reste de chaque partie pour joueur 1'''
        if periode == '1':
                return 8
        if periode == '2':
                return 5
        if periode == '3':
                return 4
             
    

def pion_reste_j2():
        '''indiquer nombre de pion reste de chaque partie pour joueur 2'''
        if periode == '1':
                return 8
        if periode == '2':
                return 5
        if periode == '3':
                return 2



def image_cord(cord):
        ''' l'image de cordonnees saisis '''
        return grille[tous_lignes.index(cord[0])][int(cord[1])-1]



def cord_depart():
        '''return la cordonne depart'''
        print("tapez la case depart:")
        depart = saisir_coordonnees()
        if joueur_courant == 1:
                if image_cord(depart) == w or image_cord(depart) == dv:
                        print("vous avez mal choisi la case départ !! resaisiez le:")
                        return cord_depart()
        if joueur_courant == 2:
                if image_cord(depart) == b or image_cord(depart) == dv:
                        print("vous avez mal choisi la case départ !! resaisiez le:")
                        return cord_depart()  
        return depart


def cord_arrive():
        '''return la cordonne arrive'''
        print("tapez la case arrivee:")
        arrive = saisir_coordonnees()
        return arrive



# FONCTIONS DE VERIFICATION LA REGLE


#verifier_contenu
def verifier_contenu_noncaptu(depart,arrive):
        '''verifier le contenu de deux cases choisis par joueur1 pour deplacement simple'''
        if (image_cord(depart) == b and image_cord(arrive) == dv) or (image_cord(depart) == w and image_cord(arrive) == dv):
                return True
        return False


def verifier_contenu_captu(depart,arrive):
        '''verifier le contenu de deux cases choisis par joueur 1 pour deplacement capture'''
        if (image_cord(depart) == b and image_cord(arrive) == w) or (image_cord(depart) == w and image_cord(arrive) == b):
                return True
        return False


#verifier_direction
def verifier_direction(depart,arrive):
        '''verifier si les position de case depart et celle arrivé sont bien orthogonales'''
        if (depart[0] == arrive[0] and depart[1] != arrive[1])  \
                or (depart[1] == arrive[1] and depart[0] != arrive[0]):
                return True
        return False


#verifier_distance 1 ou 2
def verifier_distance_noncaptu(depart,arrive):
        '''verifier la distance de case depart et celle arrivé pour deplacement simple'''
        if abs(int(arrive[1])-int(depart[1])) == 1 \
                or abs(tous_lignes.index(arrive[0])-tous_lignes.index(depart[0])) == 1:
                return True
        return False


def verifier_distance_captu(depart,arrive):
        '''verifier la distance de case depart et celle arrivé pour deplacement capture'''
        if abs(int(arrive[1])-int(depart[1])) == 2 \
                or abs(tous_lignes.index(arrive[0])-tous_lignes.index(depart[0])) == 2:
                return True
        return False



# verifier si le joueur peut capturer le pion d'autre. 
def verifier_captu_j1(depart,arrive):
        '''verifier si joueur 1 peut capturer le pion de joueur 2'''
        if depart[0] == arrive[0]:
                if int(arrive[1]) > int(depart[1]) :
                        if grille[tous_lignes.index(depart[0])][int(depart[1])] == b:
                                return True 
                else:
                        if grille[tous_lignes.index(depart[0])][int(depart[1])-2] == b:
                                return True
                return False
        else:
                if tous_lignes.index(depart[0]) > tous_lignes.index(arrive[0]):
                        if grille[tous_lignes.index(depart[0])-1][int(depart[1])-1] == b:
                                return True
                else:
                        if grille[tous_lignes.index(depart[0])+1][int(depart[1])-1] == b:
                                return True
                return False

    
def verifier_captu_j2(depart,arrive):
        '''verifier si joueur 2 peut capturer le pion de joueur 1'''
        if depart[0] == arrive[0]:
                if int(arrive[1]) > int(depart[1]) :
                        if grille[tous_lignes.index(depart[0])][int(depart[1])] == w:
                                return True 
                else:
                        if grille[tous_lignes.index(depart[0])][int(depart[1])-2] == w:
                                return True
                return False
        else:
                if tous_lignes.index(depart[0]) > tous_lignes.index(arrive[0]):
                        if grille[tous_lignes.index(depart[0])-1][int(depart[1])-1] == w:
                                return True
                else:
                        if grille[tous_lignes.index(depart[0])+1][int(depart[1])-1] == w:
                                return True
                return False

#
### pour verifier si un type de deplacement sur des pions est possible ou pas .
#

def deplacement_simple(depart,arrive):
        '''vérifier si le pion de j1 peut deplacer de type simple de cordonnees depart à celles de arrive'''
        if verifier_contenu_noncaptu(depart,arrive) == True and verifier_direction(depart,arrive) == True \
                and verifier_distance_noncaptu(depart,arrive) == True:
                
                return True
        return False


def deplacement_captu_j1(depart,arrive):
        '''vérifier si le pion de j1 peut deplacer de type capture de cordonnees depart à celles de arrive'''
        if verifier_contenu_captu(depart,arrive) == True and verifier_direction(depart,arrive) == True \
                and verifier_distance_captu(depart,arrive) == True and verifier_captu_j1(depart,arrive) == True:
                
                return True
        return False

def deplacement_captu_j2(depart,arrive):
        '''vérifier si le pion de j1 peut deplacer de type capture de cordonnees depart à celles de arrive'''
        if verifier_contenu_captu(depart,arrive) == True and verifier_direction(depart,arrive) == True \
                and verifier_distance_captu(depart,arrive) == True and verifier_captu_j2(depart,arrive) == True:
                
                return True
        return False

# On toujour renvoie les booléens pour faciliter les véfications de fonction principales et les tests dans autre ficher.



#    
# change les valeur de cases depart et arrive et le affiche.
#

def effet_pion(depart,arrive):
        '''réaliser l'effet de deplacement'''
        l_d = tous_lignes.index(depart[0])
        c_d = int(depart[1])-1
        l_a = tous_lignes.index(arrive[0])
        c_a = int(arrive[1])-1
        if verifier_distance_noncaptu(depart,arrive) == True:
                grille[l_d][c_d],grille[l_a][c_a] = grille[l_a][c_a],grille[l_d][c_d]
        if verifier_distance_captu(depart,arrive) == True:
                grille[l_d][c_d],grille[l_a][c_a] = dv,grille[l_d][c_d]
        return afficher_grille(grille)



#
### PARTIE POUR L'IA .
#

def recuperer_les_pion_b():
        '''récuperer tous les pions de joueur 1 dans grille'''
        liste_cords_b = []
        for l in tous_lignes:
                for c in tous_colonnes2:
                        if image_cord(l+c) == b :
                                liste_cords_b.append(l+c)
        return liste_cords_b



def recuperer_les_pions_w():
        '''récuperer tous les pions de joueur 2 dans grille''' 
        liste_cords_w = []
        for l in tous_lignes:
                for c in tous_colonnes2:
                        if image_cord(l+c) == w :
                                liste_cords_w.append(l+c)
        return liste_cords_w


def les_pions_de_j2_non_bloque():
        '''récuperer les cordonnees des pions non bloqués de j2'''
        liste_cords_w = recuperer_les_pions_w()
        liste_cords_non_bloquer=[]
        for cord in liste_cords_w:
                for ls in tous_lignes:
                        for cs in tous_colonnes2:
                                case = ls+cs
                                if deplacement_simple(cord,case) == True or deplacement_captu_j2(cord,case) == True :
                                        liste_cords_non_bloquer.append(cord)
        liste_cords_non_bloquer_distinct = list(set(liste_cords_non_bloquer)) #par cette fonction, on peut supprimer les cordonnees répetées. 
        
        return liste_cords_non_bloquer_distinct



def les_pions_de_j1_non_bloque():
        '''récuperer les cordonnees des pions non bloqués de j1'''
        liste_cords_b = recuperer_les_pion_b()
        liste_cords_non_bloquer=[]
        for cord in liste_cords_b:
                for ls in tous_lignes:
                        for cs in tous_colonnes2:
                                case = ls+cs
                                if deplacement_simple(cord,case) == True or deplacement_captu_j1(cord,case) == True :
                                        liste_cords_non_bloquer.append(cord)
        liste_cords_non_bloquer_distinct = list(set(liste_cords_non_bloquer)) #par cette fonction, on peut supprimer les cordonnees répetées. 
        
        return liste_cords_non_bloquer_distinct    


                                     
#### on toujours cherche les cordonnées par façon ergodique.

# partie IA naïf

def les_cords_de_pion_depart_aleatoire():
        '''les cordonnees aleatoires de pion depart pour IA naïve'''
        liste_cords_non_bloquer = les_pions_de_j2_non_bloque()
        cord_depart = random.choice(liste_cords_non_bloquer)
        return cord_depart



def les_cords_de_deplacement_aleatoire():
        '''les cordonnees aleatoire de case arrivé pour IA naïve'''
        cords_arrive_possible = []
        cord_depart = les_cords_de_pion_depart_aleatoire()
        for l in tous_lignes:
                for c in tous_colonnes2:
                        if deplacement_simple(cord_depart,l+c) == True or deplacement_captu_j2(cord_depart,l+c) == True:
                                cords_arrive_possible.append(l+c)
        cord_arrive = random.choice(cords_arrive_possible)
        return cord_depart, cord_arrive


#
# partie IA avancé
#


def effet_pion_sans_afficher(depart,arrive):
        '''réaliser l'effet de deplacement'''
        l_d = tous_lignes.index(depart[0])
        c_d = int(depart[1])-1
        l_a = tous_lignes.index(arrive[0])
        c_a = int(arrive[1])-1
        grille[l_d][c_d],grille[l_a][c_a] = grille[l_a][c_a],grille[l_d][c_d]


        
def le_nombre_des_pions_joueur_bloque():
        '''calculer le nombre des pions bloqués de joueur '''
        liste_cords_b = recuperer_les_pion_b()
        liste_cords_b_bloque = []
        nombre_bloque_chaque_case = 0
        for cord in liste_cords_b:
                for ls in tous_lignes:
                        for cs in tous_colonnes2:
                                case = ls+cs
                                if deplacement_simple(cord,case) == False and deplacement_captu_j1(cord,case) == False :
                                        nombre_bloque_chaque_case += 1
                if nombre_bloque_chaque_case == 16:
                        liste_cords_b_bloque.append(cord)
                nombre_bloque_chaque_case = 0
        return len(liste_cords_b_bloque)



def IA_avance():
        '''le choix des cordonnees aleatoires pour IA avancé'''
        liste_depart_possible = []
        liste_arrive_possible = []  # recuperer tous cordonnées de tous possibles de deplacement. 
        liste_score = []
        indice_max_score = []
        score_init = 0
        liste_cords_non_bloquer = les_pions_de_j2_non_bloque()
        for cord in liste_cords_non_bloquer:
                for l in tous_lignes:
                        for c in tous_colonnes2:
                                if deplacement_simple(cord,l+c) == True:
                                        liste_depart_possible.append(cord)
                                        liste_arrive_possible.append(l+c)
                                        le_nombre_bloque_avant_ = le_nombre_des_pions_joueur_bloque()
                                        effet_pion_sans_afficher(cord,l+c)
                                        le_nombre_bloque_apres_ = le_nombre_des_pions_joueur_bloque()
                                        score_init += (le_nombre_bloque_apres_-le_nombre_bloque_avant_)*1.5
                                        liste_score.append(score_init)
                                        effet_pion_sans_afficher(l+c,cord)   # on change les pion back.
                                if deplacement_captu_j2(cord,l+c) == True:
                                     liste_depart_possible.append(cord)
                                     liste_arrive_possible.append(l+c)
                                     le_nombre_bloque_avant = le_nombre_des_pions_joueur_bloque()
                                     score_init += 2.5 # chaque deplacement capture possible on ajoute 2.5 points  
                                     grille[tous_lignes.index(l)][int(c)-1] = dv
                                     effet_pion_sans_afficher(cord,l+c)
                                     le_nombre_bloque_apres = le_nombre_des_pions_joueur_bloque()
                                     score_init += (le_nombre_bloque_apres-le_nombre_bloque_avant)*1.5 #chaque joueur inverse bloqué on ajoute 1.5 point
                                     liste_score.append(score_init)
                                     grille[tous_lignes.index(cord[0])][int((cord)[1])-1] = b
                                     effet_pion_sans_afficher(cord,l+c)            
                        score_init = 0                        
        score_max = max(liste_score)
        liste = []
        liste2 = []
        print('tous possibilités des départ',liste_depart_possible)
        print('tous possibilités des arrive',liste_arrive_possible)
        print('tous possibilités des score ',liste_score)
        i = 0
        while i != len(liste_score):
                if  liste_score[i]== score_max:
                        liste.append(liste_depart_possible[i])
                        liste2.append(liste_arrive_possible[i])
                        indice_max_score.append(i)
                i+=1
        print('max score est:',score_max)
        print('les indices de max score     :',indice_max_score)
        print('les départs qui a max score  :',liste)
        print('les arrives qui a max score  :',liste2)
        indice_max_score_aleatoire = random.choice(indice_max_score) # on fait un choix aléatoire dans les cordonnées qui ont meilleu score. 
        depart = liste_depart_possible[indice_max_score_aleatoire]
        arrive = liste_arrive_possible[indice_max_score_aleatoire]
        print("IA avancé choisit aléatoirement dans les scores max:",'depart:',depart,'arrive:',arrive)
        
        return depart,arrive



#
# verifier si il est fin partie.
#

# quand tous les pion qui ne sont pas bloqués egale 0 ou le nombre de pion reste moins ou égale 1,  il est defait.
def fin_partie_j1():
        '''verifier si joueur 1 est défaite'''
        liste_cords_non_bloquer = les_pions_de_j1_non_bloque()   
        if len(liste_cords_non_bloquer) == 0 or pion_reste_j1 <= 1 :
                return True
        return False

 
def fin_partie_j2():
        '''verifier si joueur 2 est défaite'''
        liste_cords_non_bloquer = les_pions_de_j2_non_bloque()
        if (len(liste_cords_non_bloquer) == 0) or (pion_reste_j2 <= 1) :
                return True
        return False



## determine si il est fin partie après deplacement
#

                
def si_fin_partie_j1_true():
        '''l'affichage si fin partie de joueur 1 est true'''
        if modele == '1':
                print(v)
                print('     joueur2: o  win !!!')
                print(v)
                print(v)
                sys.exit(0)
        elif modele == '2':
                print(v)
                print('     joueur2(IA naïve): o  win !!!')
                print(v)
                print(v)
                sys.exit(0)
        else:
                print(v)
                print('     joueur2(IA avancé): o  win !!!')
                print(v)
                print(v)
                sys.exit(0)  # Si qeulqu'un gagne le jeu , on quitte toute la programme


   
def si_fin_partie_j2_false():
        '''l'affichage si fin partie de joueur 2 est false'''
        if modele == '1':
                print('    joueur courant:  o  ','    pion reste:' ,pion_reste_j2,'    nombre de coups:',nombre_de_coups_j2)
                print(v)
        elif modele == '2':
                print('    joueur courant(IA naïve):  o  ','    pion reste:' ,pion_reste_j2,'    nombre de coups:',nombre_de_coups_j2)
                print(v)
        else:
                print('    joueur courant(IA avancé):  o  ','    pion reste:' ,pion_reste_j2,'    nombre de coups:',nombre_de_coups_j2)
                print(v)



def apres_deplacement_de_j2():
        '''les étapes après le deplacement de joueur 2'''
        if fin_partie_j1() == False:
                        print('    joueur courant:  •  ','    pion reste:' ,pion_reste_j1,'    nombre de coups:',nombre_de_coups_j1)
                        print(v)
        else:
                si_fin_partie_j1_true()


     
def apres_deplacement_de_j1():
        '''les étapes après le déplacement de joueur 1'''
        if fin_partie_j2() == False:
                si_fin_partie_j2_false()              
        else:
                print(v)
                print('     joueur1: •  win !!!')
                print(v)
                print(v)
                sys.exit(0) # Si qeulqu'un gagne le jeu , on quitte toute la programme

                
#
## pour obtenir les cordonnées de joueur 2 dépand le mode de jeu que le joueur choisi.
def obtebir_cords_j2_ou_IA():
        '''dépend la mode de jou, choisi le type pour obtenir les cordonnées de joueur 2'''
        if modele == '1':
                depart = cord_depart()
                arrive = cord_arrive()
                return depart,arrive
        elif modele == '2':
                return les_cords_de_deplacement_aleatoire()
        else:
                return IA_avance()
        
 ###FONCTIONS PRINCIPALES




##deplacement récursives entre joueur 1 et joueur 2 jusqu'un joueur d'eux gagne.
        
def deplace_j2():
        '''realiser les deplacements de joueur 2'''
        global joueur_courant
        global pion_reste_j1 # On change la type de cette variable pour pouvoir le manupiler de suite
        global nombre_de_coups_j2 # On change la type de cette variable pour pouvoir le manupiler de suite
        joueur_courant = 2
        les_cords = obtebir_cords_j2_ou_IA()
        depart = les_cords[0]
        arrive = les_cords[1]
        if deplacement_simple(depart,arrive) == True:       
                effet_pion(depart,arrive)
                nombre_de_coups_j2 +=1
                apres_deplacement_de_j2()
        elif deplacement_captu_j2(depart,arrive) == True:
                effet_pion(depart,arrive)
                pion_reste_j1 -=1
                nombre_de_coups_j2 +=1
                apres_deplacement_de_j2()                        
        else:
                print("vous pouvez pas marcher comme ça !! resaisiez les cordonnées:")
                return deplace_j2() #si le joueur mal choisit les cases, il peut resaisir.
        return deplace_j1()
        
    
  
def deplace_j1():
        '''realiser les deplacements de joueur 1'''
        global joueur_courant
        global pion_reste_j2 # On change la type de cette variable pour pouvoir le manupiler de suite
        global nombre_de_coups_j1  # On change la type de cette variable pour pouvoir le manupiler de suite
        joueur_courant = 1
        depart = cord_depart()
        arrive = cord_arrive()
        if deplacement_simple(depart,arrive) == True:
                effet_pion(depart,arrive)
                nombre_de_coups_j1 +=1
                apres_deplacement_de_j1()   # Si qeulqu'un gagne le jeu , on quitte toute la programme 
        elif deplacement_captu_j1(depart,arrive) == True:
                effet_pion(depart,arrive)
                pion_reste_j2 -=1
                nombre_de_coups_j1 +=1
                apres_deplacement_de_j1()
        else:
                print("vous pouvez pas marcher comme ça !! resaisiez les cordonnées:") #évider de choisir le pion bloqué.on demande de resaisir tous les cordonnées
                return deplace_j1()
        return deplace_j2()



def random_commence_par_j1_ou_j2():
        '''commence le tour de jeu par joueur 1 ou joueur 2'''
        if random.choice(['j1', 'j2']) == 'j1':
                print('    joueur courant:  •  ',' pion reste:' ,pion_reste_j1,'    nombre de coups:',nombre_de_coups_j1 )
                print(v)
                return  deplace_j1()
        si_fin_partie_j2_false()  
        return deplace_j2()


##### CODES PRINCIPALES



### APPEL INITIALISATION
#
#


bienvenu() # mettez ce appel en commenté quand vous exécutez la ficher des tests.

afficher_grille_init() # mettez cette ligne en commenté quand vous exécutez la ficher des tests.

modele = saisi_jeu_modele() # mettez cette ligne en commenté quand vous exécutez la ficher des tests.

periode = saisi_periode() # mettez cette ligne en commenté quand vous exécutez la ficher des tests.

grille = choisi_periode_en_commence() # mettez cette ligne en commenté quand vous exécutez la ficher des tests.

pion_reste_j1 = pion_reste_j1() # mettez ce appel en commenté quand vous exécutez la ficher des tests.

pion_reste_j2 = pion_reste_j2() # mettez ce appel en commenté quand vous exécutez la ficher des tests.

afficher_grille(grille) # mettez ce appel en commenté quand vous exécutez la ficher des tests.

#
### APPEL RECURSIVE
#

random_commence_par_j1_ou_j2() # mettez ce appel en commenté quand vous exécutez la ficher des tests.


#
##### la ligne desous est met seulment pour exécuter la ficher des tests
#grille = grille_fin  # que cette ligne doit etre activé quand vous exécutez la fiche des tests.












