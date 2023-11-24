from RechercheFichier import *
from FonctionDeBases import *

def premier_mot(mot):
    """

    :param: mot: Un mot dont on veut rechercher qui l'a dit en premier
    :return: mi_pre: le nom du président qui a énoncer le mot rechercher en premier dans son discours (ou les noms si ils l'ont prononcer en meme temps)
    
    """
    mi = -1                                                    # On initialise une variable qui va compter le nombre de mots dit par chaque président avant le mot rechercher
    mi_pre = []                                                # On initialise une liste qui contiendra le ou les noms des présidents qui ont dit se mot en premier
    for fichier in list_of_files("./cleaned", ".txt"):         # On crée un boucle qui va nous permettre d'ouvrir tous les fichiers
        with open("./cleaned/" + fichier, "r") as f:           # on ouvre le fichier sur lequel on pointe actuellement
            text = f.read()                                    # On met son contenu dans une variable
            text = text.split(" ")                             # On le transforme en liste en de mots
            i = 0                                              # On initialise une variable qui pointera sur les mots de la liste
            while text[i] != mot and i < len(text) -1:         # On crée une boucle qui va tourner tant qu'on aura pas trouver le mot recharcher ou qu'on ne sera pas a la fin du discours
                i = i+1                                        # On incrémente le pointeur de mot
            if text[i] == mot and mi==-1:                      # Si c'est la toute première fois que l'on rencontre le mot on initialise la variable mi au nombre de mots qu'il y a eu avant le mot recharcher
                mi = i
                mi_pre.append(get_names(0, fichier))           # Et on ajoute dans la liste le nom des présidents qui l'on dit
            elif text[i] == mot and i < mi:                    # Sinon si se n'est pas la première fois que l'on rencontre se mot et que le nombre de mots qu'il y a eu avant est inférieur a la valeur stocker dans la variable mi on met la nouvelle valeur dans celle-ci
                mi = i
                mi_pre = [get_names(0, fichier)]               # Et on réinitialise la liste avec uniquement le nom du nouveau président
            elif text[i] == mot and i == mi:                   # Enfin, si se n'est pas la première fois que l'on rencontre le mot et que le nombre de mots dit avant est exactement égal a la valeur stockée dans mi alors on ajoute le nom du nouveau président avec l'autre déja présent dans la liste
                mi = i
                mi_pre.append(get_names(0, fichier))
    return set(mi_pre)                                         # Pour terminer on retourne le nom de tous les présidents sans doublons qui ont dit le mot rechercher en premier
#Commande de test
#print(premier_mot("messieurs"))
