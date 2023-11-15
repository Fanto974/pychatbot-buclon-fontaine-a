from TFIDF import *
from RechercheFichier import * 

def highest_tfidf(directory="./cleaned/"):
    tf_idf = tfidf(directory)
    dico_key = list(idf().keys())
    liste_documents = list_of_files(directory, ".txt")
    highest_word = []
    maxi = 0
    nb_mot = 0
    nb_document = 0
    for l in tf_idf:
        for val in l:
            if val > maxi:
                maxi = val
                highest_word = [(dico_key[nb_mot], liste_documents[nb_document])]
            elif val == maxi:
                highest_word.append((dico_key[nb_mot], liste_documents[nb_document]))
            nb_document = (nb_document+1)%8
        nb_mot+=1
    return highest_word
