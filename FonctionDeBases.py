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
    for val in text:
        if "A" <= val <= "Z":
            speech_minimized += chr(ord(val) + 32)
        else:
            speech_minimized += val
    return speech_minimized


def lower_files(directory="./speech/", end_directory="./cleaned/cleaned_"):
    """
    :description: La foncion va mettre en minuscules les fichiers du dossier speech et les ranger dans ./cleaned/ avec un nom tel que "cleaned_ NOM DU FICHIER"
    """
    k = 0
    for file in list_of_files(directory, ".txt"):
        list_speech = []
        with open(directory + file, "r") as np:
            discours = np.read()
            list_speech.append(minimize_text(discours))
            np.close()
        with open(end_directory + file, "w") as np:
            np.write(list_speech[k])


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


# print(apostrophe("l",-1))


def suppr_SpeCara():
    """

    :return: les textes du dossier cleaned sans caractères spéciaux
    """
    l = -1              # Permet le remplacement de l'aposrtophe avec une variable intermédiaire
    list_fichiers = list_of_files("./cleaned", ".txt")      #crée une liste de tous les fichiers contenus dans cleaned
    for fichier in list_fichiers:           #ouvre les fichiers de cette liste un par un
        with open("./cleaned/" + fichier, "r") as fc:
            fichier_chaine = fc.read()
            chaine_SansCaraSpe = ""             # Crée une chaine de caractère sans caracrères spéciaux
            for i in range(len(fichier_chaine)):
                if "a" <= fichier_chaine[i] <= "z":             # Si c'est une lettre normal on la met dans la nouvelle chaine
                    chaine_SansCaraSpe += fichier_chaine[i]
                else:
                    if fichier_chaine[i] == "'":                # Sinon on traite autrement
                        chaine_SansCaraSpe += apostrophe(fichier_chaine[i - 1], l)      # Si c'est une apostrophe on apelle la fonction dédiée
                        l *= -1
                    else:
                        chaine_SansCaraSpe += " "           # Sinon on remplace par un espace
        chaine_SansCaraSpe2 = ""                    #on crée une nouvelle chaine afin de supprimer les doublons d'espaces
        for i in range(len(chaine_SansCaraSpe) - 1):
            if chaine_SansCaraSpe[i + 1] == " " and chaine_SansCaraSpe[i] == " ":
                chaine_SansCaraSpe2 += ""
            else:
                chaine_SansCaraSpe2 += chaine_SansCaraSpe[i]

        with open("./cleaned/" + fichier, "w") as fc:
            fc.write(chaine_SansCaraSpe2)
# suppr_SpeCara()
