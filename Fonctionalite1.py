from TFIDF import *

def NonImportant():
    dico_key = list(idf().keys())
    matrice = tfidf()
    list_mots_non_important = []
    for liste in range(len(matrice)):
        mot = 0
        for val in range(8):
            if matrice[liste][val] != 0:
                mot += 1
        if mot == 0:
            list_mots_non_important.append(dico_key[liste])
    return list_mots_non_important
