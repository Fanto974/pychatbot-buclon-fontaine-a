from RechercheFichier import *
from FonctionDeBases import *

def premier_mot(mot):
    mi = -1
    mi_pre = []
    for fichier in list_of_files("./cleaned", ".txt"):
        with open("./cleaned/" + fichier, "r") as f:
            text = f.read()
            text = text.split(" ")
            i = 0
            while text[i] != mot and i < len(text) -1:
                i = i+1
            if text[i] == mot and mi==-1:
                mi = i
                mi_pre.append(get_names(0, fichier))
            elif text[i] == mot and i < mi:
                mi = i
                mi_pre = [get_names(0, fichier)]
            elif text[i] == mot and i == mi:
                mi = i
                mi_pre.append(get_names(0, fichier))
    return set(mi_pre)
#Commande de test
#print(premier_mot("messieurs"))
