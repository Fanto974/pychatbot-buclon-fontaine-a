from Fonctionalités_Partie1.Fonctionalite1 import *
from FonctionsDeBase2 import *


def who_said(directory="./cleaned/", word="Nation"):
    """
    :desc: Fonction qui dit quel président on prononcer un mot donné
    """
    word = minimize_text(word)             #Enleve les majuscules
    word = tokenisation(word)[0]
    tf_idf = tfidf(directory)               #La matrice Tf-IDF
    dico_key = list(idf().keys())           #La liste de tout les mots de TF-IDF
    liste_names = get_names(directory, 0, 0)      #Le nom de tout les présidents
    time_said = {}                          
    people_max = []
    #La valeur maxi et l'id auxquels il est associé
    maxi = 0
    id = 0
    for file in list_of_files(directory, ".txt"):
        name = get_names(0, file)
        with open(directory + file, "r") as f:
            dico = tf(f.read())
            for val in dico:
                if val == word:
                    time_said[name] = dico[word]

    for val in time_said.keys():
        if time_said[val] > maxi:
            maxi = time_said[val]
            people_max = [val]
        elif time_said[val] == maxi:
            people_max.append(val)
    return [people_max, list(time_said.keys())]
#print(who_said("./cleaned/", "Nation"))
