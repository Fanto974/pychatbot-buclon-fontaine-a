from TFIDF import *
from FonctionDeBases import *

def NonImportant6():
    """
    Affiche les mots que tout le monde a évoqué en excluant manuellemant les mots réelment non importants tels que les pronoms personnels, les conjonctions etc...
    """
    dico_key = list(idf().keys())
    matrice = tfidf()
    list_mots_non_important = []
    mot_nul = ["je","tu","il","elle","on","nous","vous","ils","elles","est","un","une","le","la","les","et","du","des","de","me","ce","se","aux","a","dans","par","pour","en","vers","avec","sans","sous","sur","son","mais","qui","que","quoi","dont","ou"]
    for liste in range(len(matrice)):
        mot = 0
        for val in range(8):
            if matrice[liste][val] != 0:
                mot += 1
        if mot == 0:
            if dico_key[liste] not in mot_nul:
                list_mots_non_important.append(dico_key[liste])
    return list_mots_non_important
