from TFIDF import *
from FonctionDeBases import *

def NonImportant():
    dico_key = list(idf().keys())                                # On crée une liste contenant tous les mots de tous les discours a partir de la fonction idf()
    matrice = tfidf()                                            # On crée une variable matrice qui stock toute la matrice générée par le tfidf()
    list_mots_non_important = []                                 # Enfin, on crée une liste qui va contenir tous les mots dit non importants. PS : c'est la variable que l'on va renvoyer
    for liste in range(len(matrice)):                            # On parcours par index toute la matrice
        occurence_mot = 0                                        # On initalise a chaque tour de boucle, soit a chaque nouveau mot une variable qui va compter le nombre de texte dans lesquels le mots n'a pas un tfidf de 0.
        for val in range(8):                                     # Comme il y a 8 textes on va donc regarder 8 valeurs différentes
            if matrice[liste][val] != 0:                         # Si le mot dans le texte que l'on regarde a un tfidf différent de 0 on ajoute 1 a la variable occurence_mot
                occurence_mot += 1
        if occurence_mot == 0:                                   # Après avoir parcourus les 8 valeurs d'un mot, si la variable occurence_mot est toujours a 0 c'est que pour chaque texte, ce mot a un tfidf de 0. Il n'est donc pas important
            list_mots_non_important.append(dico_key[liste])      # Dans ce cas, on l'ajoute a la liste des mots non importants
    return list_mots_non_important                               # Et enfin, on affiche cette liste
    
