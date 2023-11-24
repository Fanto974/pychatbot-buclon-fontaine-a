from Fonctionalite1 import *
from HighestTFIDF import * 
from Fonctionalité3 import *
from Fonctionalite4 import *
from Fonctionalite5 import *
from RechercheFichier import *
from FonctionDeBases import *
from Fonctionalite6 import *


def menu():
    choice = 1
    while choice != 0:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        line = "______________________________________________________________________________________________"
        print(line)
        print("MENU:\n - 0: Quitter\n - 1: Liste des mots avec un TF-IDF de 0\n - 2: Affiche le mot avec le TF-IDF le plus élevé\n - 3:Affcihe le mot le plus répété par un président\n - 4:Indique le noms des présidents ayant prononcé un certain mot\n - 5:Indique le premier président à parler d'un mot donné\n - 6: Indique les mots dont tout le monde à parlé")
        print(line+"\n\n\n")
        choice = int(input("Votre choix : "))
        if choice == 0:
            pass
        elif choice == 1:
            print("\nLes mots avec un TF-IDF de 0 sont:")
            for val in NonImportant():
                print(val, end = ", ")
            print("\n\n")
        elif choice == 2:
            print("Le mot avec le plus élevé TF-IDF est: ")
            high = highest_tfidf()
            print(high[0][0])
            print("\nPrononcé dans :")
            print(high[0][1])
            print("\nPar "+get_names(0, high[0][1]))
            print("\n\n")
        elif choice == 3:
            cible = input("\nQuel président voulez-vous cibler : ")
            print("Le mot le plus prononcé par "+cible+" est : "+Plus_mot(cible))
            print("\n\n")
        elif choice == 4:
            mot = input("\nQuel mot voulez-vous analyser : ")
            who_s = who_said("./cleaned/",mot)
            print("Le mot "+mot+" a été prononcé par :")
            for val in who_s[1]:
                print(val, end=", ")
            print("\n\nIl a été prononcé le plus par : ")
            for val in who_s[0]:
                print(val)
            print("\n")
        elif choice == 5:
            mot = minimize_text(input("\nQuel mot voulez-vous analyser : "))
            print("Le premier président à parler de "+mot+" est : ", end ="")
            for val in premier_mot(mot):
                print(val)
        elif choice == 6:
            print("A part les mots non importants. \nLes mots que tout les présidents prononcent sont : ")
            mots = NonImportant6()
            for val in mots:
                print(val, end = ", ")
        else:
            print("Veuillez entrez une autre valeur, cette valeur n'est pas prise en charge.")
        if choice != 0:
            pause = input()
menu()
