from RechercheFichier import *


def get_names(directory="./speech/"):
    """
    :param : Dossier contenant les fichier des discours
    :return: list_name: liste des noms de chaque présients ayant fait un discours que l'on posséde en fichier

    :description: Recupère les noms de tt les présidents
    """
    list_files = list_of_files(directory, ".txt")
    set_of_name = {"Initialisation du set"}
    set_of_name.clear()
    for file in list_files:
        if 47 < ord(file[-5]) < 58:  # Si le 5 eme caractère est un chiffre:
            set_of_name.add(file[:-5][
                            11:])  # On ne le prend pas dans le nom car c'est un indicateur du numéro de discourd tel que le 1 dans "Chirac1.txt"

        else:  # Sinon si ce n'est pas un chiffre:
            set_of_name.add(file[:-4][11:])  # On prend prend le 5eme caractere car il fait parti du nom

    return list(set_of_name)


def associe(list_noms):
    """

    :param list_noms: une liste des noms SANS DOUBLONS des présidents voulu
    :return: les noms et prénoms de tous les présidents ayant fait des discours

    :descirption: Permet pour chaque nom de président de lui donner un prénom
    """
    with open("Nom_Prenom.txt","r") as np:  # Ouvre le fichier contenant la liste de tout les présidents francais ayant existés
        list_NomsPrenoms = []  # Crée une liste qui associra le nom et les prénoms
        list_NomPrenom = np.readlines()
        for i in range(len(list_NomPrenom)):  # Parcours les prénoms de tous les présidents du fichier
            a = list_NomPrenom[i].split(" : ")
            if a[0] in list_noms:  # Si un nom est également dans la liste de nom pris en paramètre:
                list_NomsPrenoms.append(
                    list_NomPrenom[i][:-1])  # la liste finale apprend le nom et le prénom du président en question
        return list_NomsPrenoms


def print_unique(directory, extension):
    """

    :param: Dossiers contenant les fichier

    :description: On affiche les noms des présidents en évitants les doublons.
    """
    print(get_names())  # Les doublons sont déjà gérer par les sets dans get_names


def minimize_text(text):
    """
    
    :param text: chaine de caracteres avec des majuscules, minuscules et caracteres sopeciaux
    :return: une chaine de caratere sans majuscules

    :description: la fonction réduit les majuscules en minuscules
    """
    speech_minimized = ""
    for val in text:                                 #Pour chaque caractères du texte
        if "A" <= val <= "Z":                        #Si la valeur est un caractère majuscule
            speech_minimized += chr(ord(val) + 32)   #On la transforme en son equivalent en minuscules
        else:    
            speech_minimized += val                  #Sinon on ajoute directement le caractère
    return speech_minimized
    
def lower_files(directory = "./speech/", end_directory="./cleaned/cleaned_"):
    """
    :param: Le dossier depuis lequel on prend les fichier et celui dans lequel on stock les nouveaux fichiers
    :description: La foncion va mettre en minuscules les fichiers du dossier speech et les ranger dans ./cleaned/ avec un nom tel que "cleaned_ NOM DU FICHIER"
    """
    k= 0
    for file in list_of_files(directory, ".txt"):          #Pour chaque fichier du dossier donné
        list_speech = []
        with open(directory+file, "r") as np:              #On ouvre le fichier du dossier en lecture
            discours = np.read()
            list_speech.append(minimize_text(discours))    #On ajoute a la liste l'equivalent du fichier en minuscules
            np.close()
        with open(end_directory+file, "w") as np:
            np.write(list_speech[k])                        #On écrit dans le nouveau fichier le texe en minuscules

def apostrophe(lettre, l):
    """
    :param lettre, l: La lettre qui précède l'appostrophe, la variable permettant un changement du remplacement 1 fois sur 2.
    :return: Str: remplace l'apostrophe.

    :description: Permet de remplacer l'appostrophe non pas par un espace mais en prenant en compte la lettre precedente afin de remplacer au mieux pour ne pas fausser les vecteurs TF IDF des mots
    """
    if lettre == "l":
        if l == -1:
            return "e "
        else:
            return "a "
    else:
        return "e "

def suppr_SpeCara():
    l = -1
    liste_e = ["é","è","ê","ë"]
    liste_a = ["à","â"]
    list_fichiers = list_of_files("./cleaned", ".txt")
    for fichier in list_fichiers:
        with open("./cleaned/" + fichier, "r", encoding='utf8') as fc:
            fichier_chaine = fc.read()
            chaine_SansCaraSpe = ""
            for i in range(len(fichier_chaine)):
                if "a" <= fichier_chaine[i] <= "z":
                    chaine_SansCaraSpe += fichier_chaine[i]
                else:
                    #print(fichier_chaine[i])
                    if fichier_chaine[i] == "'":
                        chaine_SansCaraSpe += apostrophe(fichier_chaine[i-1], l)
                        l *= -1
                    elif fichier_chaine[i] in liste_e:
                        chaine_SansCaraSpe += "e"

                    elif fichier_chaine[i] in liste_a:
                        chaine_SansCaraSpe += "a"

                    elif fichier_chaine[i] == "ù":
                        chaine_SansCaraSpe += "u"

                    elif fichier_chaine[i] == "ç":
                        chaine_SansCaraSpe += "c"

                    elif fichier_chaine[i] == "ô":
                        chaine_SansCaraSpe += "o"

                    else:
                        chaine_SansCaraSpe += " "
        chaine_SansCaraSpe2 = ""
        for i in range(len(chaine_SansCaraSpe) -1):
            if chaine_SansCaraSpe[i + 1] == " " and chaine_SansCaraSpe[i] == " ":
                chaine_SansCaraSpe2 += ""
            else:
                chaine_SansCaraSpe2 += chaine_SansCaraSpe[i]

        with open ("./cleaned/" + fichier, "w") as fc:
            fc.write(chaine_SansCaraSpe2)
