"""
    Ce fichier est essentiel puisqu'il permet a l'utilisateur d'utiliser toutes les fonctionnalités qui lui ont été atribuées ainsi que le Chat Bot
"""
from Fonctionalités_Partie1.Fonctionalite2 import *
from Fonctionalités_Partie1.Fonctionalité3 import *
from Fonctionalités_Partie1.Fonctionalite4 import *
from Fonctionalités_Partie1.Fonctionalite5 import *
from Fonctionalités_Partie1.Fonctionalite6 import *
from FonctionsDeBase2 import *
from os import *
"""
Document permettant d'accéder aux différentes fonctions du programme tels que le chatbot et 
Les fonctinnalitées de la partie 1
"""
global chatBot_directory
chatBot_directory = "./Dossiers_Thematiques/speech/"

def menu():
    """
    Permet à l'utilisateur de choisir les fonctions qu'ils veulent tester ou bien lui donne accès au chatbot
    """
    directory = chatBot_directory
    for file in list_of_files("./cleaned_chatBot", ".txt"):
        os.remove("./cleaned_chatBot/" + str(file))
    lower_files(directory, "./cleaned_chatBot/cleaned_")
    suppr_SpeCara("./cleaned_chatBot/")
    directory = "./Dossiers_Thematiques/speech/"
    choice = "1"
    while choice != "0":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n"*15)
        line = "______________________________________________________________________________________________"
        print(line)
        print("MENU:\n - Bot: accès au chatbot\n - 0: Quitter\n - 1: Liste des mots avec un TF-IDF de 0\n - 2: Affiche le mot avec le TF-IDF le plus élevé\n - 3: Affiche le mot le plus répété par un président\n - 4: Indique le noms des présidents ayant prononcé un certain mot\n - 5: Indique le premier président à parler d'un mot donné\n - 6: Indique les mots dont tout le monde à parlé\n")
        print(line+"\n\n\n")
        choice = input("Votre choix : ")
        if choice == "0":
            pass
        elif tokenisation(choice)[0] == "bot":
            chat_bot()
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
            who_s = who_said("./cleaned/", mot)
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
        else:
            print("Veuillez saisir une autre valeur, cette valeur n'est pas prise en charge")
        if choice != "0":
            input("Pressez entrée")

def chat_bot():
    """
    Permet à l'utilisateur de communiquer avec les differntes versions de chatbot et d'en modifier les directory de références
    """
    global chatBot_directory
    line = "______________________________________________________________________________________________"
    directory_clean = "./cleaned_chatBot"
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n"*15)
    print(line)
    print("Bienvenue dans le menu du chat bot,\nNous avons 2 mode de réponse différrent\n 0: Retour\n 1 - Mode réponse rapide\n 2 - Mode de réponse complexe\n 3 - Info sur les 2 modes\n 4 - Changer de base de donnée \n          Directory actuel: ",chatBot_directory)
    print(line)
    choix = input("Choix : ")
    if choix == "1":
        question = ""
        print("\n\n0 - Quitter le chat bot\nSinon énoncez votre question")
        while question != "0":
            question = input("Vous : ")
            if question != "0":
                print("\nChatBot : ", respond(question, chatBot_directory), "\n")
    elif choix == "2":
        question = ""
        print("\n\n0 - Quitter le chat bot\nSinon énoncez votre question")
        while question != "0":
            question = input("Vous : ")
            if "note" in regr(tokenisation(question)," ") and "merite"in regr(tokenisation(question)," "):
                print("\nChatBot : ", end= " ")
                print("Ils mériteraient la note de 20/20 sans aucun doute\n")
            elif question != "0":
                print("\nChatBot : ", end= " ")
                rep = reponse_finale(question, chatBot_directory, directory_clean)
                print(rep[0], "\n")
                if rep[1] == False:
                    politesse("ajout")
    elif choix == "3":
        print("\n\nLe 1er mode affiche la phrase contenant la première occurence du mot de la question ayant le score TF-IDF le plus élevé\nDans le document ayant le plus grande similitude trouvé à, l'aide de la similarit cosinus\n\n\nLe 2eme mode va récuperer le même document que la 1ere methode\nVa calculer le vecteur TF-IDF de chaque phrase du texte\nPuis comparé celle-ci avec le TF-IDF de la questionà l'aide la similarté cosinus\nCela prend donc plus de temps mais donne une réponse trouvé d'un manière beaucoup plus cohérente.\n\n")
    elif choix == "4":
        print("Directory : ", chatBot_directory)
        print("Liste des directory disponibles: ")
        for file in list_of_files("./Dossiers_Thematiques", ""):
            print("     -",file)
        print("Entrez 0 pour ne pas le modifier")
        val = input("Dans quel directory voulez-vous utiliser le chat bot : ")
        if val != "0":
            directory = "./Dossiers_Thematiques/" + val + "/"
            
            for file in list_of_files("./cleaned_chatBot", ".txt"):
                os.remove("./cleaned_chatBot/" + str(file))
            lower_files(directory, "./cleaned_chatBot/cleaned_")
            suppr_SpeCara("./cleaned_chatBot/")
            print("Corpus changé avec succés ! ")
            print(directory)
            chatBot_directory = directory
    elif choix == "0":
        pass
    else:
        print("Veuillez saisir une autre valeur celle-ci n'est pas prise en charge")
        chat_bot()

menu()
