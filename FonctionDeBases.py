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
