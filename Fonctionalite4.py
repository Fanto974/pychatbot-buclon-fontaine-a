from TFIDF import *
from FonctionDeBases import *

def who_said(directory="./cleaned/",word="Nation"):
    """
    :desc: Fonction qui dit quel président on prononcer un mot donné
    """
    tf_idf = tfidf(directory)               #La matrice Tf-IDF
    dico_key = list(idf().keys())           #La liste de tout les mots de TF-IDF
    liste_names = get_names(directory, 0, 0)      #Le nom de tout les présidents
    time_said = {}                          
    people_max = []

    #La valeur maxi et l'id auxquels il est associé
    maxi = 0
    id = 0

    for i in range(len(dico_key)-1):                            #Pour chaque mot dans le dictionnaire
        if minimize_text(dico_key[i]) == minimize_text(word):   #Si le mot est celui que l'on recherche
            id = i                                              #On note son id puis on quitte la boucle
            break

    for i in range(len(tf_idf[id])):                    #Pour chaque documents dans le ligne TF-IDF du mot cherché
        if tf_idf[id][i]!=0:
            if liste_names[i] in time_said.keys():          #Si le nom du président est déjà dans la liste de ceux qui ont dit le mot
                time_said[liste_names[i]] += tf_idf[id][i]  #
            else:
                time_said[liste_names[i]] = tf_idf[id][i]          
    for val in time_said.keys():
        if time_said[val] > maxi:
            maxi = time_said[val]
            people_max = [val]
        elif time_said[val] == maxi:
            people_max.append(val)
    return [people_max, list(time_said.keys())]
#print(who_said("./cleaned/", "Nation"))
