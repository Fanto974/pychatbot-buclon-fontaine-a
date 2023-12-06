from FonctionDeBases import *
from TFIDF import *
from math import *

def tokenisation(text):
    text = minimize_text(text) + " "
    l = -1
    liste_e = ["é","è","ê","ë"]
    liste_a = ["à","â"]
    chaine_SansCaraSpe = ""
    for i in range(len(text)):
        if "a" <= text[i] <= "z":
            chaine_SansCaraSpe += text[i]
        else:
            if text[i] == "'":
                chaine_SansCaraSpe += apostrophe(text[i-1], l)
                l *= -1
            elif text[i] in liste_e:
                chaine_SansCaraSpe += "e"

            elif text[i] in liste_a:
                chaine_SansCaraSpe += "a"

            elif text[i] == "ù":
                chaine_SansCaraSpe += "u"

            elif text[i] == "ç":
                chaine_SansCaraSpe += "c"

            elif text[i] == "ô":
                chaine_SansCaraSpe += "o"

            else:
                 chaine_SansCaraSpe += " "
    chaine_SansCaraSpe2 = ""
    for i in range(len(chaine_SansCaraSpe)-1):
        if chaine_SansCaraSpe[i + 1] == " " and chaine_SansCaraSpe[i] == " ":
            chaine_SansCaraSpe2 += ""
        else:
            chaine_SansCaraSpe2 += chaine_SansCaraSpe[i]
    return chaine_SansCaraSpe2.split(" ")

def intersection(text, directory = "./cleaned"):
    list_in_corpus = list(idf(directory).keys())
    l_text = tokenisation(text)
    l_intersection = []
    for word in l_text:
        if word in list_in_corpus:
            l_intersection.append(word)
    return l_intersection

def compose_matrice(matrice):
    new_matrice = [[0]*len(matrice) for i in range(len(matrice[0]))]
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            new_matrice[j][i] = matrice[i][j]
    return new_matrice

def TFIDF_Qestion(text):
    M = []
    list_mots = list(idf("./cleaned").keys())
    list_mots_Question = intersection(text)
    tf_motQuestion = tf(text)
    idf_motCorpus = idf("./cleaned")
    for i in list_mots:
        if i in list_mots_Question:
            M.append(tf_motQuestion[i] * idf_motCorpus[i])
        else:
            M.append(0)
    return M
#print(TFIDF_Qestion("bonjour jour jour messieurs abaissement dames le climat change"))

def norme(vector):
    sum = 0
    for val in vector:
        sum+=val
    return sqrt(sum)

def scalaire(Va, Vb):
    sum = 0
    if len(Va) == len(Vb):
        for i in range(len(Va)):
            sum += Va[i]*Vb[i]
        return sum
    else:
        raise TypeError("Les 2 vecteurs doivent avoir autant de valeurs")


def similar(matrice_question,directory = "./cleaned"):
    list_norme = [[0] for i in range(len(compose_matrice(tfidf(directory))))]
    norme_q = norme(matrice_question)
    matrice = compose_matrice(tfidf(directory))

    for i in range(len(matrice)):
        list_norme[i] = norme(matrice[i])

    list_similarities = []
    for i in range(len(matrice)):
        list_similarities.append(scalaire(matrice_question, matrice[i])/norme_q*list_norme[i])
    return list_similarities

def doc_pertinent(matrice_question, list_nomFichier = list_of_files("./cleaned", "txt")):
    liste_similarite = similar(matrice_question)
    max = [0, 0]
    for i in range(len(liste_similarite)):
        if liste_similarite[i] > max[0]:
            max[0] = liste_similarite[i]
            max[1] = i
    if max[0] == 0:
        return "Il n'y a aucun document plus pertinent"
    else:
        return list_nomFichier[max[1]]
#print(doc_pertinent(TFIDF_Qestion("les doit est bien")))

def most_impo_q(text):
    max = 0
    id = 0
    question_tfidf = TFIDF_Qestion(text)
    for i in range(len(question_tfidf)):
        if question_tfidf[i] > max:
            max = question_tfidf[i]
            id = i
    return list(idf().keys())[id]
#print(most_impo_q("bonjour jour doit messieurs abaissement dames le climat change"))
