from FonctionDeBases import *
from TFIDF import *

def Plus_mot(president):
    """
    :param : Le nom d'un président
    :return: mot_max[1]: Le mot le plus répéter par se président
    
    :description: Permet d'identifier le mot le plus dit par un président
    """
    list_fichier = list_of_files("./cleaned", "txt")                # Récupère tous les noms des fichiers textes contenus dans le dossier "cleaned"
    mot_max = [0, ""]                                               # On initialise une liste qui aura 2 valeurs, le nombre d'occurence la plus élever de tous les mots qu'on aura parcourus dit par un président et une deuxième valeur qui contiendra se mot en question
    for i in range(len(list_fichier)):                              # On fait une boucle qui permettera d'ouvrir tous les fichiers
        with open("./cleaned/" + list_fichier[i], "r") as fi:       # On ouvre le fichier ciblé actuellement
            nom = get_names(-1, list_fichier[i])                    # On récupère grâce a la fonction get_name() le nom du président du fichier que l'on a ouvert
            if minimize_text(nom) == minimize_text(president):      # On verifie que le discours que l'on étudie actuellement a bien été prononcer par le président saisi par l'utilisteur
                text = fi.readline()                                # On en extrait le contenu si c'est le cas
                dico_text = tf(text)                                # On récupère un dictionnaire qui contient tous les mots et leurs occurences du discours que l'on est en train d'étudier
                for j in list(dico_text.keys()):                    # On parcours se dictionnaire
                    if dico_text[j] > mot_max[0]:                   # Si le mot qu'on est en train de regarder a plus d'occurence que le mot stocké actuellement dans la variable mot-max, on met se mot a la place en deuxième position et son nombre d'occurences en première position 
                        mot_max[0] = dico_text[j]
                        mot_max[1] = j
    return mot_max[1]                                               # Enfin, on retourne le mot répéter le plus de fois par le président demander par l'utilisateur
