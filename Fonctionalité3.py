from RechercheFichier import *
from FonctionDeBases import *
from TFIDF import *

def Plus_mot(president):
    list_fichier = list_of_files("./cleaned", "txt")
    mot_max = [0, ""]
    for i in range(len(list_fichier)):
        with open("./cleaned/" + list_fichier[i], "r") as fi:
            nom = get_names(-1, list_fichier[i])
            if minimize_text(nom) == minimize_text(president):
                text = fi.readline()
                dico_text = tf(text)
                for j in list(dico_text.keys()):
                    if dico_text[j] > mot_max[0]:
                        mot_max[0] = dico_text[j]
                        mot_max[1] = j
    return mot_max[1]
