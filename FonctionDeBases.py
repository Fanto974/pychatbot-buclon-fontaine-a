from RechercheFichier import *


def get_names(list_files):
    """
    :param list_files: Liste des fichier des discours
    :return: list_name: liste des noms de chaque présients ayant fait un discours que l'on posséde en fichier
    
    :description: Recupère les noms de tt les présidents
    """
    set_of_name = {"Initialisation du set"}
    set_of_name.clear()
    for file in list_files:
        if 47 < ord(file[-5]) < 58:             # Si le 5 eme caractère est un chiffre:
            set_of_name.add(file[:-5][11:])     # On ne le prend pas dans le nom car c'est un indicateur du numéro de discourd tel que le 1 dans "Chirac1.txt"
        
        else:                                   # Sinon si ce n'est pas un chiffre:
            set_of_name.add(file[:-4][11:])     # On prend prend le 5eme caractere car il fait parti du nom
    
    return list(set_of_name)


def associe(list_noms):
    """

    :param list_noms: une liste des noms SANS DOUBLONS des présidents voulu
    :return: les noms et prénoms de tous les présidents ayant fait des discours
    """
    with open("Nom_Prenom.txt","r") as np:  # Ouvre le fichier contenant la liste de tout les présidents francais ayant existés
        list_NomsPrenoms = []               #Crée une liste qui associra le nom et les prénoms
        list_NomPrenom = np.readlines()
        for i in range(len(list_NomPrenom)):  # Parcours les prénoms de tous les présidents du fichier
            a = list_NomPrenom[i].split(" : ")
            if a[0] in list_noms:  # Si un nom est également dans la liste de nom pris en paramètre:
                list_NomsPrenoms.append(list_NomPrenom[i][:-1])  # la liste finale apprend le nom et le prénom du président en question
        return list_NomsPrenoms

def print_unique(directory, extension):
    """

    :param: Dossiers contenant les fichier
    
    :description: On affiche les noms des présidents en évitants les doublons.
    """
    print(get_names(list_of_files(directory, extension)))# Les doublons sont déjà gérer par les sets dans get_names
