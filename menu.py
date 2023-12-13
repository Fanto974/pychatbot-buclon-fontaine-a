from Fonctionalités_Partie1.Fonctionalite2 import *
from Fonctionalités_Partie1.Fonctionalité3 import *
from Fonctionalités_Partie1.Fonctionalite4 import *
from Fonctionalités_Partie1.Fonctionalite5 import *
from Fonctionalités_Partie1.Fonctionalite6 import *
from FonctionsDeBase2 import *
from os import *

#print(respond_better("On doit manger"))
def menu():
    choice = "1"
    directory = "./Dossiers_Thematiques/speech/"
    directory_clean = "./cleaned"
    while choice != "0":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        line = "______________________________________________________________________________________________"
        print(line)
        print("MENU:\n - Bot: accès au chatbot\n - 0: Quitter\n - 1: Liste des mots avec un TF-IDF de 0\n - 2: Affiche le mot avec le TF-IDF le plus élevé\n - 3: Affiche le mot le plus répété par un président\n - 4: Indique le noms des présidents ayant prononcé un certain mot\n - 5: Indique le premier président à parler d'un mot donné\n - 6: Indique les mots dont tout le monde à parlé\n - 7: Accéder au chat bot")
        print(line+"\n\n\n")
        choice = input("Votre choix : ")
        if choice == "0":
            pass
        elif tokenisation(choice)[0] == "bot":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(line)
            print("Bienvenue dans le menu du chat bot,\nNous avons 2 mode de réponse différrent\n 0: Retour\n 1 - Mode réponse rapide\n 2 - Mode de réponse complexe\n 3 - Info sur les 2 modes\n 4 - Changez les répertoires d'analyses \n    Directory actuel: ",directory)
            print(line)
            choix = input("Choix : ")
            if choix == "1":
                question = ""
                print("\n\n0 - Quitter le chat bot\nSinon énoncez votre question")
                while question != "0":
                    question = input("Vous : ")
                    print("\nChatBot : ",respond(question,directory), "\n")
            elif choix == "2":
                question = ""
                print("\n\n0 - Quitter le chat bot\nSinon énoncez votre question")
                while question != "0":
                    question = input("Vous : ")
                    print("\nChatBot : ",respond_better(question,directory,directory_clean), "\n")
            elif choix == "3":
                print("\n\nLe 1er mode affiche la phrase contenant la première occurence du mot de la question ayant le score TF-IDF le plus élevé\nDans le document ayant le plus grande similitude trouvé à, l'aide de la similarit cosinus\n\n\nLe 2eme mode va récuperer le même document que la 1ere methode\nVa calculer le vecteur TF-IDF de chaque phrase du texte\nPuis comparé celle-ci avec le TF-IDF de la questionà l'aide la similarté cosinus\nCela prend donc plus de temps mais donne une réponse trouvé d'un manière beaucoup plus cohérente.\n\n")
            elif choix == "4":
                print("Directory : ",directory)
                print("Entrez 0 pour ne pas modifier le directory")
                val = input("Nouveau directory : ")
                if val != "0":
                    directory = "./Dossiers_Thematiques/"+val+"/"
                    for file in list_of_files("./cleaned", ".txt"):
                        os.remove("./cleaned/"+str(file))
                    lower_files(directory+"/")
                    suppr_SpeCara()
                    print("Corpus changé avec succés ! ")
                    print(directory)
        elif choice == "1":
            print("\nLes mots avec un TF-IDF de 0 sont:")
            for val in NonImportant():
                print(val, end = ", ")
            print("\n\n")
        elif choice == "2":
            print("Le mot avec le plus élevé TF-IDF est: ")
            high = highest_tfidf()
            print(high[0][0])
            print("\nPrononcé dans :")
            print(high[0][1])
            print("\nPar "+get_names(0, high[0][1]))
            print("\n\n")
        elif choice == "3":
            cible = input("\nQuel président voulez-vous cibler : ")
            if Plus_mot(cible) != "":
                print("Le mot le plus prononcé par "+cible+" est : "+Plus_mot(cible))
            else:
                print("Erreur : Le président n'a pas été trouvé. Verifiez l'orthographe et si c'est un nom de président valide")
            print("\n\n")
        elif choice == "4":
            mot = input("\nQuel mot voulez-vous analyser : ")
            who_s = who_said("./cleaned/",mot)
            if who_s[1] != []:
                print("Le mot "+mot+" a été prononcé par :")
                for val in who_s[1]:
                    print(val, end=", ")
                print("\n\nIl a été prononcé le plus par : ")
                for val in who_s[0]:
                    print(val)
                print("\n")
            else:
                print("le mot a été prononcer par aucun des présidents dans leurs discours")
        elif choice == "5":
            mot = minimize_text(input("\nQuel mot voulez-vous analyser : "))
            if premier_mot(mot) != set([]):
                if len(premier_mot(mot)) == 1:
                    print("Le premier président à parler de "+mot+" est : ", end ="")
                    for val in premier_mot(mot):
                        print(val)
                else:
                    print("Les premiers a parler de " + mot + " sont : ", end = "")
                    for val in premier_mot(mot):
                        print(val, end = ", ")
            else:
                print("Le mot que vous recherchez n'a été dit par aucun président")
        elif choice == "6":
            print("A part les mots non importants. \nLes mots que tout les présidents prononcent sont : ")
            mots = NonImportant6()
            for val in mots:
                print(val, end = ", ")
        elif choice == "7":
            quest = input("Posez votre question :")
            while quest == "":
                quest = input("Veuillez écrire une question !")
            rep = reponse_finale(quest)
            if rep[1] == False:
                politesse("ajout")
        else:
            print("Veuillez entrez une autre valeur, cette valeur n'est pas prise en charge.")
        if choice != "0":
            pause = input("APPUYEZ SUR ENTREE")
menu()
